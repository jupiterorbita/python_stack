from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    print('\n= = = index = = =')
    return render(request, 'loginregistration/index.html')


def registration(request):
    print('\ntouch regitration========')
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], bday=request.POST['bday'], password=hashed_pw)
            request.session['id'] = User.objects.get(email=request.POST['email']).id
            messages.success(request, "WELCOME FROM REGISTRATION")
            return redirect('/success')


def login(request):
    print('\ntouch LOGIN============')
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            request.session['id'] = User.objects.get(email=request.POST['email']).id
            messages.success(request, "WELCOME FROM LOGIN")
            return redirect('/success')


def success(request):
    print('\ntouch SUCCESS=========')
    if 'id' in request.session:
        userDB = User.objects.get(id=request.session['id'])
        context = {
            'user': userDB,
        }
        return render(request, 'loginregistration/success.html', context)
    else:
        return redirect('/')


def logout(request):
    print('\n= = = LOGOUT = = =')
    request.session.clear()
    return redirect('/')