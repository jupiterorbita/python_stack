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
        # print('=-=-=-=- got post data =>', request.POST)
        # print("*"*50)
        errors = User.objects.registration_validator(request.POST)
        # print('erros? = ', errors)
        if len(errors):
            for key, value in errors.items(): # if the errors object contains anything, loop through each key-value pair and make a flash message
                messages.error(request, value)
            return redirect('/')
        else:
            # print('\n---------------- PASSED OK validations')
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], bday=request.POST['bday'], password=hashed_pw)
            # print('\n---------------- user should be inserted')
            return redirect('/success')


def login(request):
    print('\ntouch LOGIN============')
    if request.method == 'POST':
        print('=-=-=-=-= got post data =>', request.POST)
        errors = User.objects.login_validator(request.POST)
        print('\n\n', errors, '\n\n')
        if len(errors):
            for key, value in errors.items(): # if the errors object contains anything, loop through each key-value pair and make a flash message
                messages.error(request, value)
            return redirect('/')
        else:
            return redirect('/success')


def success(request, id):
    print('\ntouch SUCCESS=========')
    return render(request, 'loginregistration/success.html')


def logout(request):
    print('\n= = = LOGOUT = = =')
    request.session.clear()
    return redirect('/')