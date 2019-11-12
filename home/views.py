from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib import messages



# Create your views here.

def login_user(request):
    user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
    # handle error cases, inactive users, ...

    login_return = None

    if user is not None:
        login(request, user)
        return render(request, 'home.html')
    else:
        messages.error(request, 'Login failed.')
        print('Login Failed')
        #Failed. Send message and log?

    if login_return == None:
        print('User not in database.')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)


def support(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
    return render(request, 'support.html')

def mail(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'mail.html', context)


def hmi(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'hmi': '10.0.%s.9' % settings.TEAM,
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'hmi.html', context)


def notes(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM,
        'myip': '10.0.%s.6' % settings.TEAM
    }
    return render(request, 'notes.html', context)


def files(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'files.html', context)


def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'home.html', context)
