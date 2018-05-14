from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    print('\n ===========\n number from /number =', number)
    response = 'placeholder to display blog '+str(number)
    return HttpResponse(response)

def edit(request, number2):
    print('\n ===========\n number from /number/edit =', number2)
    response = 'placeholder to edit blog '+str(number2)
    return HttpResponse(response)

def destroy(request, number):
    print('\n ===========\n number from /number/delete =', number)
    return redirect('/')