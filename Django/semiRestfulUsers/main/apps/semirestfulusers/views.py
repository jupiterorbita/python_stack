from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages


def index(request):
    print('\n========  inside INDEX  ======')
    userDB = User.objects.all().order_by("-created_at")
    context = {
        'users': userDB
    }
    return render(request, "semirestfulusers/index.html", context)
def new(request):
    print('\n========  inside NEW  ======')
    # calls the new method to display a form allowing users to create a new user. This will need a template.
    return render(request, "semirestfulusers/new.html")

def edit(request, id):
    print('\n========  inside EDIT  ======')
    getid = User.objects.get(id=id)
    context = {
        'user': getid
    }
    return render(request, "semirestfulusers/edit.html", context)

def update(request):
    print('\n========  inside UPDATE  ======')
    if request.method == 'POST':     # pass the post data to the method we wrote and save the response in a variable called errors
        id = request.POST['id']
        print('-=-=-=-==-- =- =- -=- ID ', id)
        print('=====', request.POST['first_name'])
        print('=====', request.POST['last_name'])
        print('=====', request.POST['email'])
        errors = User.objects.user_validator(request.POST)
        print('erros? = ', errors)
        if len(errors):
            print('INSIDE ERRORS @@@@@@@')
            for key, value in errors.items(): # if the errors object contains anything, loop through each key-value pair and make a flash message
                print('#@$@#@#$@#$@# inside the key kanrue error')
                messages.error(request, value)
            return redirect('/users/'+id+'/edit') # redirect the user back to the form to fix the errors

        else:
            u = User.objects.get(id=id)
            u.fist_name = request.POST['first_name']
            u.last_name = request.POST['last_name']
            u.email = request.POST['email']
            u.save()
        return redirect('/')






def show(request, id):
    print('\n========  inside SHOW  ======')    
    userDB = User.objects.get(id=id)
    context = {
        'users': userDB
    }
    return render(request, "semirestfulusers/show.html", context)

def create(request):
    print('\n========  inside CREATE  ======')
    if request.method == 'POST':     # pass the post data to the method we wrote and save the response in a variable called errors
        print('=====', request.POST['first_name'])
        print('=====', request.POST['last_name'])
        print('=====', request.POST['email'])
        errors = User.objects.user_validator(request.POST)
        print('erros? = ', errors)
        if len(errors):
            print('INSIDE ERRORS @@@@@@@')
            for key, value in errors.items(): # if the errors object contains anything, loop through each key-value pair and make a flash message
                print('#@$@#@#$@#$@# inside the key kanrue error')
                messages.error(request, value)
            return redirect('/users/new') # redirect the user back to the form to fix the errors
        
        else:
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            user.save()
        return redirect('/')

def destroy(request, id):
    print('\n========  inside DESTROY  ======')
    User.objects.get(id=id).delete()
    return redirect('/')

