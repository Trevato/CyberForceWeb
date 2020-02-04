from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib import messages



# Create your views here.

def login_user(request):
    user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
    # handle error cases, inactive users, ...

    print('Test')

    if user is not None:
        try:
            login(request, user)
        except Exception:
            messages.error(request, 'Login failed.')
        return render(request, 'login.html', context)
    else:
        print('Login Failed')
        #Failed. Send message and log?

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return render(request, 'logout.html')


def support(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
    return render(request, 'support.html')

def mail(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'ftpsrv': 'ftp.cybatiworks.com'
    }
    return render(request, 'mail.html', context)


def hmi(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'hmi': '10.0.%s.9' % settings.TEAM,
        'ftpsrv': 'ftp.cybatiworks.com'
    }
    return render(request, 'hmi.html', context)


def notes(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'ftpsrv': 'ftp.cybatiworks.com',
        'myip': 'cybatiworks.com'
    }
    return render(request, 'notes.html', context)


def files(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'ftpsrv': 'ftp.cybatiworks.com'
    }
    return render(request, 'files.html', context)


def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'ftpsrv': 'ftp.cybatiworks.com'
    }
    return render(request, 'home.html', context)
