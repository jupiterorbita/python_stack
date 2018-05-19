from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print('\n === inside index ===')
    return render(request, 'likesbooks/index.html')