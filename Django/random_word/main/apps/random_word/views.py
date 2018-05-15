from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

print('== inside views.py==')
# the index function is called when root is visited

def index(request):

    if 'name' not in request.session:
        request.session['name'] = 1
    else:
        request.session['name'] +=1
    print('\n======', request.session['name'])

    context = {
        'unique_txt': get_random_string(length=14)
        }
    unique_txt = get_random_string(length=14)

    print('\n=-=-=-=- random txt is -=-=-=- ==> ', unique_txt, '\n')
    return render(request, "random_word/index.html", context)


def reset(request):
    request.session.clear()
    # session.flush()
    return redirect('/')

