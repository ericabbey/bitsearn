import qrcode
import qrcode.image.svg
from hashlib import sha256
import re

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from dashboard.models import dashboard, user_info, option
from geneology.views import get_auth_upliner, get_upliner
from .forms import WalletForm
from .models import btcAddr, transaction, missed


digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')

def check_bc(bc):
    bcbytes = decode_base58(bc, 25)
    return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]



@login_required(login_url='/login/')
def stats(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    trans = transaction.objects.all
    pending = transaction.objects.filter(Q(user=request.user)|Q(to=request.user), state="pending")
    miss= missed.objects.filter(was_to=request.user)
    context = {
    'profile': profile,
    'info': info,
    'trans': trans,
    "pending":pending,
    'missed': miss
    }
    return render (request, 'profile/stats.html', context )


def generateQr(instance):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )
    qr.add_data(instance.newAddr)
    qr.make(fit=True)

    filename = '%s_qrcode_%i.png' %(instance.user.username, instance.changeCount)
    img = qr.make_image()
    img.save('../media_cdn/qrcode/' + filename)
    source = '../media/qrcode/' + filename
    return source

@login_required(login_url='/login/')
def wallet(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    form = WalletForm(request.POST or None)
    addr_count = btcAddr.objects.get(user=request.user).changeCount
    msg = ""
    data = ""
    if request.method == "POST":
        if form.is_valid:
            password = request.POST.get("password")
            address = request.POST.get("address")
            encoded = request.user.password
            pwd_valid = check_password(password, encoded)
            if pwd_valid:
                btc_length = len(address)
                v_addr=check_bc(address)
                if btc_length == 25 or btc_length == 34 and v_addr:
                    b = btcAddr.objects.filter(user=request.user)
                    btc = btcAddr.objects.get(user=request.user)
                    qrCode = generateQr(btc)
                    if addr_count == 0:
                        addr_count = addr_count + 1
                        b.update(newAddr=address, changeCount=addr_count, qrcode=qrCode)
                        data = "Bitcoin wallet added successfully"
                    else:
                        addr_count = addr_count + 1
                        b.update(newAddr=address, oldAddr=b[0].newAddr, changeCount=addr_count, qrcode=qrCode)
                        data = "Bitcoin wallet updated successfully"

                else:
                    msg = "Invalid bitcoin wallet address"
                    form = WalletForm()
            else:
                msg = "password invalid"
                form = WalletForm()
    addr = btcAddr.objects.filter(user=request.user)
    context = {
    'profile': profile,
    'info': info,
    'msg': msg,
    'addr': addr,
    'data': data
    }
    return render (request, 'profile/wallet.html', context )

def amount_to_send(level):
    amount = ""
    if level == 0:
        amount = 0.002
    elif level == 1:
        amount = 0.003
    elif level == 2:
        amount = 0.02
    elif level == 3:
        amount = 0.45
    return amount

@login_required(login_url='/login/')
def upgrade(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    op = option.objects.filter(user=request.user)
    upline = get_auth_upliner(profile.level, request)
    addr = btcAddr.objects.filter(user=upline)
    if addr:
        addr = btcAddr.objects.get(user=upline)
    if request.method == "POST":
        if request.is_ajax():
            val = request.POST.get("value")
            name = request.POST.get("name")
            if name == 'dsd':
                op.update(dsd=val)
            elif name == 'dsi':
                op.update(dsi=val)
        else:
         transac = request.POST.get("trid")
        amount = request.POST.get("amnt")
        transaction.objects.create(user=request.user, to=upline, trans_id=transac, amount=amount,level=profile.level, state="pending")
    nxt_level = profile.level + 1
    context = {
    'profile': profile,
    'info': info,
    'address':addr,
    'ops':op,
    'nxt_level': nxt_level,
    'upliner': upline,
    'amount': amount_to_send(profile.level)
    }
    return render (request, 'profile/upgrade.html', context )
