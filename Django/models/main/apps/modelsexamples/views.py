from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "This is Models Django DB - Examples / Migrations / Foreign-key / commands etc..."
    return HttpResponse(response)