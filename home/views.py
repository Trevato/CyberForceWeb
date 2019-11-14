from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

@csrf_exempt
def login_user(request):
    print('Login view.')
    user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
    # handle error cases, inactive users, ...

    print('User authenticated.')

    if user is not None:
        try:
            login(request, user)
        except Exception:
            messages.error(request, 'Login failed.')
        context = {
            'ftpsrv': '10.0.%s.8' % settings.TEAM
        }
        print('User logged in.')
        return render(request, 'files.html', context)
    else:
        print('Login Failed')
        #Failed. Send message and log?

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return render(request, 'logout.html')


def support(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'support.html')

def mail(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')

    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'mail.html', context)


def hmi(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')

    context = {
        'hmi': '10.0.%s.9' % settings.TEAM,
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'hmi.html', context)


def notes(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')

    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM,
        'myip': '127.0.0.1'
    }
    return render(request, 'notes.html', context)


def files(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')

    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'files.html', context)


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')

    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'home.html', context)
