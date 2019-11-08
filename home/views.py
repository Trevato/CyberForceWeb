from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login


# Create your views here.

def login_user(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    # handle error cases, inactive users, ...

    login_return = login(request, user)

    if login_return == None:
        print('User not in database.')

    return render(request, 'login.html')

def mail(request):
    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'mail.html', context)


def hmi(request):
    context = {
        'hmi': '10.0.%s.9' % settings.TEAM,
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'hmi.html', context)


def notes(request):
    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM,
        'myip': '10.0.%s.6' % settings.TEAM
    }
    return render(request, 'notes.html', context)


def files(request):
    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'files.html', context)


def index(request):
    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'home.html', context)
