from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import jwt


def authtest(request) :

    if request.user.is_authenticated() :

        return HttpResponse("<h3>Welcome %s</h3><a href='/logout/'>Logout</a>" % request.user.email)

    else :
        return HttpResponse("<a href='%s'>Login</a>" % settings.BITIUM_LOGIN_URL or "/")

def deauth(request) :
    logout(request)
    return redirect('/')

def auth(request) :

    user = authenticate(payload=request.GET.get('jwt'))

    if user is not None :
        login(request, user)
        return redirect(settings.BITIUM_REDIRECT_URL)
    else :
        return HttpResponse('Fail')
        return redirect(settings.BITIUM_LOGIN_URL)

