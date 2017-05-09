from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dashboard.models import dashboard, user_info
from geneology.models import tree, Descendant


@login_required(login_url='/login/')
def geneo(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    user = dashboard.objects.get(user=request.user)
    ref_id = user.ref_id
    children = Descendant.objects.filter(upliner=request.user)
    context = {
        'profile': profile,
        'info': info,
        'ref': ref_id,
        'children': children
    }
    return render(request, 'profile/geneology.html', context)


@login_required(login_url='/login/')
def treeview(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    ref_id = profile.ref_id
    # trees
    p1 = tree.objects.filter(p1=request.user)\
        .select_related('doner__dashboard',)

    instance = tree.objects.all()
    context = {
        'profile': profile,
        'info': info,
        'ref': ref_id,
        'p1': p1,
        'tree': instance
    }
    return render(request, 'profile/list_view.html', context)


@login_required(login_url='/login/')
def expiring(request):
    profile = dashboard.objects.get(user=request.user)
    info = user_info.objects.get(user=request.user)
    children = Descendant.objects.filter(upliner=request.user)
    ref_id = profile.ref_id
    context = {
        'profile': profile,
        'ref': ref_id,
        'info': info,
        'children': children,
    }
    return render(request, 'profile/expire.html', context)

def get_upliner(level, request):
    parent = tree.objects.get(doner=request.user, )
    upliner = ""
    if level == 0:
        upliner = parent.p1
    elif level == 1:
        upliner = parent.p2
    elif level == 2:
        upliner = parent.p3
    elif level == 3:
        upliner = parent.p4
    return upliner

def get_auth_upliner(level, request):
    parent = get_upliner(level, request)
    p_level = parent.dashboard.level
    print(" parent level: "+str(p_level))
    print("level: "+str(level))
    exp = p_level >= level
    print(exp)
    while not exp:
        level = level + 1
        print(level)
        if level <= 3:
            parent = get_upliner(level, request)
            p_level = parent.dashboard.level
            exp = p_level >= level
        else:
            parent = User.objects.get(username="superAdmin")
            exp = True
            up = parent
            return up

    print("level: "+str(level))
    up = get_upliner(level,request)
    return up
