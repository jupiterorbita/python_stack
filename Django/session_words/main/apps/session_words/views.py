from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request, "session_words/index.html")


def process(request):
    # debugHelp('PROCESS method')
    print('=-=-=-=-=- inside process =-=-=--=')
    if request.method == "POST":
        print('-=-=-=-=-=- POST receieved \n')
        print('\n === post ==> ', request.POST)
        print(request.POST['word'])

    datetime = {
        'date': strftime("%Y-%m-%d", gmtime()),
        'time': strftime("%H:%M %p", gmtime())
    }
    request.session['datetime'] = datetime

    # color
    if 'color' in request.POST:
        request.session['color'] = request.POST['color']
    else: 
        request.session['color'] = 'black'
       
    # is big check
    if 'isbig' not in request.POST:
        request.session['isbig'] = 12
    else:
        request.session['isbig'] = 24

    # make a list and put obj in it to append
    temp_list = request.session['words']
    temp_list.append({
        "word": request.POST['word'], 
        "color": request.session['color'], 
        "isbig": request.session['isbig'],
        'date': datetime['date'],
        'time': datetime['time']
        })
    request.session['words'] = temp_list

    return redirect('/', datetime)
    

def reset(request):
    request.session.clear()
    return redirect('/')
