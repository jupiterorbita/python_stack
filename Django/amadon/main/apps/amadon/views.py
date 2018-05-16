from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'amadon/index.html')


def buy(request):
    print('\n = = got post = = =\n')
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'items' not in request.session:
        request.session['items'] = 0

    if request.method == "POST":
        if request.POST['product_id'] == '111':
            tshirt = int(request.POST['tshirt']) * 19.99
            item_tshirt = int(request.POST['tshirt'])
        else:
            tshirt = 0
            item_tshirt = 0

        if request.POST['product_id'] == '222':
            book = int(request.POST['book']) * 49.99
            item_book = int(request.POST['book'])
        else:
            book = 0
            item_book = 0

        if request.POST['product_id'] == '333':
            cup = int(request.POST['cup']) * 4.99
            item_cup = int(request.POST['cup'])
        else:
            cup = 0
            item_cup = 0
          
        request.session['items'] += item_tshirt + item_book + item_cup
        request.session['total'] += tshirt + book + cup
        request.session['current'] = tshirt + book + cup

        return redirect('/amadon/checkout')
    else:
        return redirect('/')

def checkout(request):
    print('\n inside CHECKOUT =-=-=-==-=---=- \n')
    return render(request, 'amadon/checkout.html')

def clear(request):
    request.session.clear()
    return redirect('/')