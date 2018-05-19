from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages


def index(request):   
    courses = Course.objects.all().order_by('-created_at')
    context = {
        'courses': courses
        }
    return render(request, "courses/index.html", context)


def add(request):
    print('\n========  inside CREATE  ======')
    if request.method == 'POST':     # pass the post data to the method we wrote and save the response in a variable called errors
        print('===== name ==>', request.POST['name'])
        print('===== desc ==>', request.POST['desc'])
        errors = Course.objects.course_validator(request.POST)
        print('$$$$ errors? ====> ', errors)
        if len(errors):
            print('INSIDE ERRORS @@@@@@@')
            for key, value in errors.items():   # if the errors object contains anything, loop through each key-value pair and make a flash message
                print('#@$@#@#$@#$@# inside the key kanrue error')
                messages.error(request, value)
            return redirect('/')   # redirect the user back to the form to fix the errors
        else:
            course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
            course.save()
        return redirect('/')


def delete(request, id):
    print('=-=-=-=-=- DELETE =-=--=-=--=')
    print(id)
    # courseDB = User.objects.get(id=id)
    context = {
        'courseDD': Course.objects.get(id=id)
    }
    return render(request, "courses/delete.html", context)


def destroy(request, id):
    print('\n========  inside D E S T R O Y  ======')
    print('ID ID ID => ', id)
    # print('@ @ @ @ request.POST["id"] =-=-=-- ID ==>', request.POST['id'])
    # if request.method == 'POST':
    Course.objects.get(id=id).delete()
    return redirect('/')