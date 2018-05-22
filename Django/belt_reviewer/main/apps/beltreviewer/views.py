from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    print('\n = = = inside INDEX ("/") = = =')
    return render(request, 'beltreviewer/index.html')


def login(request):
    print('\n = = = inside LOGIN_METHOD ("/") = = =')
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            request.session['id'] = User.objects.filter(email=request.POST['email'])[0].id
            request.session['name'] = User.objects.filter(email=request.POST['email'])[0].name
            messages.success(request, 'Welcome from LOGIN!!!')
            return redirect('/books')


def registration(request):
    print('\n = = = inside REGISTRATION_METHOD ("/") = = =')
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=hashed_pw)
            request.session['id'] = User.objects.filter(email=request.POST['email'])[0].id
            request.session['name'] = User.objects.filter(email=request.POST['email'])[0].name
            messages.success(request, 'Welcome fromm REGISTRATION!!!')
            return redirect('/books')


def books(request):
    if 'id' in request.session:
        print('\n = = = inside BOOKS ("/books") = = = /books.html')
        # show all books avail
        bookDB = Book.objects.all().order_by("-created_at")
        bookreveiw = Book.objects.get(id=22).reviews.all()
        context = {
            'books': bookDB
        }
        return render(request, 'beltreviewer/books.html', context)
    else:
        return redirect('/')



def add_book(request):
    if 'id' in request.session:
        print('\n = = = inside ADD_BOOK ("/add_book") /add_book.html = = =')
        return render(request, 'beltreviewer/add_book.html')
    else:
        return redirect('/')


def add_book_method(request):
    if 'id' in request.session:
        print('\n = = = inside ADD_BOOK_METHOD ("/add_book") method only  = = =')
        #logic for adding a book from a user
        if request.method == 'POST':
            print(request.POST)
            errors = Book.objects.book_validator(request.POST)
            print(errors)
            if len(errors):
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/add_book')
            else:
                errors = Review.objects.review_validator(request.POST)
                new_book = Book.objects.create(title=request.POST['title'], author=request.POST['author'], creator=User.objects.get(id=request.session['id']))
                print('WHAT IS NEWBOOK.ID >>!>>!>!>>>!>>!> ', new_book.id)
                if len(errors):
                    for key, value in errors.items():
                        messages.error(request, value)
                    return redirect('/add_book')
                else:
                    Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=new_book, user=User.objects.get(id=request.session['id']))
                    
                    print('***** UPLOAD SUCCESS ******')
                    return redirect('/book_review/'+str(new_book.id))
    else:
        return redirect('/')

def book_review(request, id):
    if 'id' in request.session:
        print('\n = = = inside BOOK_REVIEW ("/book_review") /book_review.html = = =')
        # you see the book you want to review
        bookDB = Book.objects.get(id=id)
        reviewDB = Book.objects.get(id=id).reviews.all()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ USERS")
        users = User.objects.get(id=4).reviews
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ USERS")
        print(users)
        context = {
            'books': bookDB,
            'reviews': reviewDB,
            'users': users
        }
        return render(request, 'beltreviewer/book_review.html', context)
    else:
        return redirect('/')

def add_book_review(request):
    if 'id' in request.session:
        print('\n = = = inside add_book_review method = = =')
        if request.method == 'POST':
            book = Book.objects.get(id=request.POST['book_id']).id
            print('\n=-=-=-= book =', book)
            Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=Book.objects.get(id=book), user = User.objects.get(id=request.session['id']))
            return redirect('/book_review/'+str(book))
    else:
        return redirect('/')

def user(request, id):
    if 'id' in request.session:
        print('\n = = = inside USER ("/user") = = =')
        user = User.objects.get(id=id)
        reviews = User.objects.get(id=id).reviews.all()
        print('what is this?@@@@@@@@@@@@@ ', reviews)
        context = {
            'users': user,
            'reviews': reviews
        }
        print('$$$$$$$$ context ===>', context)
        return render(request, 'beltreviewer/user.html', context)
    else:
        return redirect('/')

def logout(request):
    print('\n !!! LOGOUT method !!!!("/logout")')
    request.session.clear()
    return redirect('/')
