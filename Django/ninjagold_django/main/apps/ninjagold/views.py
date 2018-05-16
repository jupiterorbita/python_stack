from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime


def index(request):
    print('\n\n inside index == = == = = == ')
    return render(request, "ninjagold/index.html")


def process_money(request):
    print('\n\n inside PROCESS MONEY == = == = = == \n')

    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'msg' not in request.session:
        request.session['msg'] = []

    # datetime = {
    #     'date': strftime("%Y-%m-%d", gmtime()),
    #     'time': strftime("%H:%M %p", gmtime())
    # }
    # request.session['datetime'] = datetime

    date = str(strftime("%Y-%m-%d", gmtime()))
    time = str(strftime("%H:%M %p", gmtime()))

    if request.method == "POST":
        if request.POST['building'] == 'farm':
            farm_gold = random.randrange(10, 20)
            request.session['gold'] += farm_gold
            msg = "you got "+str(farm_gold)+" gold from FARM -- "+time+", "+date
        
        elif request.POST['building'] == 'cave':
            cave_gold = random.randrange(5, 10)
            request.session['gold'] += cave_gold
            msg = "you got "+str(cave_gold)+" gold from cave -- "+time+", "+date


        elif request.POST['building'] == 'house':
            house_gold = random.randrange(2, 5)
            request.session['gold'] += house_gold
            msg = "you got "+str(house_gold)+" gold from house -- "+time+", "+date


        elif request.POST['building'] == 'casino':
            casino_gold = random.randrange(-50, 50)
            request.session['gold'] += casino_gold
            msg = "you got "+str(casino_gold)+" gold from casino -- "+time+", "+date

        msg_list = request.session['msg']
        msg_list.insert(0 ,{
            'msgs': msg
        })
        request.session['msg'] = msg_list

        return redirect('/')

    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')