from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password

from extra.models import Action, Notif_Count
from financial.models import transaction
from geneology.models import tree
from .models import (dashboard,
                     option,
                     user_info,
                     Testiment,
                     )
from .forms import imageForm, SupportForm

def progress(request, lev):
    trees = tree.objects.all()
    if lev == 0:
        tr = trees.filter(p1=request.user)
    elif lev == 1:
        tr = trees.filter(p2=request.user)
    elif lev == 2:
        tr = trees.filter(p3=request.user)
    elif lev == 3:
        tr = trees.filter(p4=request.user)
    count = tr.count
    return count


def received_amount(request, lev, amt):
    amt_rec = 0.00
    rec = transaction.objects.filter(to=request.user , amount=amt, level=lev)
    for r in rec:
        amt_rec = amt_rec + float(r.amount)
    return amt_rec


def total_amount(tp):
    print(tp)
    if tp == 'n':
        val = 3
    elif tp == 'p':
        val = 10
    elif tp == 'd':
        val = 100
    elif tp == 's':
        val = 10000
    max = val * ((1*0.002)+(3*0.003)+(9*0.02)+(27*0.45))
    return max


@login_required(login_url='/login/')
def profile_index(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    sponsor = user_info.objects.get(user=profile.sponsor)
    sponsor_op = option.objects.get(user=profile.sponsor)
    joined = request.user.date_joined
    sent = transaction.objects.filter(user=request.user)
    actions = Action.objects.exclude(user=request.user)
    actions = actions[:6]
    notif_count = Notif_Count.objects.get(target=request.user)
    amt_sent = 0.00
    for s in sent:
        amt_sent = amt_sent + float(s.amount)
    received = transaction.objects.filter(to=request.user)
    amt_rec = 0.00
    for r in received:
        amt_rec = amt_rec + float(s.amount)
    tr = tree.objects.all()
    amt = {
        'lev1': received_amount(request, 0, 0.002),
        'lev2': received_amount(request, 1, 0.003),
        'lev3': received_amount(request, 2, 0.02),
        'lev4': received_amount(request, 4, 0.45)
    }
    lev = {
        'lev1': progress(request, 0 ),
        'lev2': progress(request, 1 ),
        'lev3': progress(request, 2 ),
        'lev4': progress(request, 3 )
    }
    context = {
        's_option': sponsor_op,
        'profile': profile,
        'joined': joined,
        'info': info,
        'sponsor': sponsor,
        'sent':  amt_sent,
        'received': amt_rec,
        'l': lev,
        'a': amt,
        'total': total_amount(profile.acc_type),
        'actions': actions,
        'notification': notif_count
    }
    return render(request, 'profile/index.html', context)


@login_required(login_url='/login/')
def profile_settings(request):
    info = user_info.objects.get(user=request.user)
    imgForm = imageForm(request.POST or None, request.FILES or None, instance=info)
    msg = ""
    if imgForm.is_valid():
        img = imgForm.save(commit=False)
        print(imgForm.cleaned_data.get("user_image"))
        img.save()
    if request.POST:
        val = request.POST.get("value")
        name = request.POST.get("name")
        op = option.objects.filter(user=request.user)
        if name == 'show_soc':
            op.update(show_soc=val)
        elif name == 'autos':
            op.update(autos=val)
        elif name == 'allowemail':
            op.update(allowemail=val)
        elif name == 'showpp':
            op.update(show_pp=val)
        elif name == 'shownum':
            op.update(show_num=val)
        faceb = request.POST.get('fb')
        twitt = request.POST.get('tw')
        gplus = request.POST.get('gp')
        linkn = request.POST.get('in')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        old_password = request.POST.get('old_password')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if old_password and password and cpassword:
            if old_password:
                if password:
                    if cpassword:
                        print("all entered")
                        u = User.objects.get(username=request.user.username)
                        valid = u.check_password(old_password)
                        if valid:
                            if password == cpassword:
                                u.set_password(password)
                                u.save()
                                authenticate(username=request.user.username, password=password)
                            else:
                                msg = "password confirmation did not match"
                                print(msg)
                        else:
                            msg = " The current password you entered in wrong "
                            print(msg)
                    else:
                        msg = "You did not confirm your password"
                else:
                     msg = "You did not enter any password"
            else:
                msg = "Please enter your current password"
        else:
            msg = "Fill the fields before submiting"
        if faceb:
            user_info.objects.filter(user=request.user).update(fb_link=faceb)
        if twitt:
            user_info.objects.filter(user=request.user).update(twi_link=twitt)
        if gplus:
            user_info.objects.filter(user=request.user).update(gm_link=gplus)
        if linkn:
            user_info.objects.filter(user=request.user).update(lin_link=linkn)
        if name:
            dashboard.objects.filter(user=request.user).update(name=name)
        if email:
            dashboard.objects.filter(user=request.user).update(email=email)
        if phone:
            dashboard.objects.filter(user=request.user).update(phone=phone)
        if country:
            dashboard.objects.filter(user=request.user).update(country=country)

    profile = dashboard.objects.get(user=request.user)
    op = option.objects.get(user=request.user)
    info_nw = user_info.objects.get(user=request.user)
    usr_sponsor = profile.sponsor
    joined = request.user.date_joined
    context = {
        'profile': profile,
        'info': info_nw,
        'joined': joined,
        'option': op,
        'sponsor': usr_sponsor,
        'msg': msg
    }
    return render(request, 'profile/profile.html', context)


@login_required(login_url='/login/')
def ext_profile(request, name=None):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    extUser = User.objects.get(username=name)
    extUserProfile = get_object_or_404(dashboard, user=extUser)
    context = {
        'profile': profile,
        'info': info,
        'ext': extUserProfile
    }
    return render(request, 'profile/ext-profile.html', context)

@login_required(login_url='/login/')
def testiment(request):
    testimony = Testiment.objects.all()
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    context = {
        'testimony': testimony,
        'profile': profile,
        'info': info
    }
    return render(request, 'profile/testimonial.html', context)


@login_required(login_url='/login/')
def new_test(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    if request.method == "POST":
        msg = request.POST.get("msg")
        if msg:
            Testiment.objects.create(user=request.user, msg=msg)
            return redirect("profile:testiment")
    context = {
        'profile': profile,
        'info': info
    }
    return render(request, 'profile/add-test.html', context )


@login_required
def support(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    form = SupportForm(request.POST or None)
    print(form)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    else:
        form = SupportForm()
    context = {
    'profile': profile,
    'info': info,
    'form': form
    }
    return render(request, 'profile/support.html', context )

@login_required
def news(request):
    return render(request, 'profile/news.html', {})
