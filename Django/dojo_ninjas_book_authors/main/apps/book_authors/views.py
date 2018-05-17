from django.shortcuts import render, HttpResponse, redirect
# from book_authors import models
# from book_authors.models import *
  # the index function is called when root is visited
def index(request):
    #check
    # book1 = Book.objects.get(id=1)
    # book2 = Book.objects.get(id=2)
    # this_author = Author.objects.get(id=1)
    # this_author.books.add(book1)
    # this_author.books.add(book2)
    # print(this_author.books.all)
    # context = {"authors": Author.objects.all()}
    # return render(request, "book_authors/index.html", context)
    return render(request, "book_authors/index.html")