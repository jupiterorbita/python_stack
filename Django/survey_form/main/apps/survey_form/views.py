from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    print('########### inside index #########')
    return render(request, 'survey_form/index.html')
    # response = "Hello, I am your first request!"
    # return HttpResponse(response)


def process(request):
    print('=-=-=- inside process =-=-=-=')
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    if request.method == "POST":
        print("*"*50)
        print('counter ==> ', request.session['counter'])
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['location'])
        print(request.POST['language'])
        print(request.POST['comment'])
        print("*"*50)

        request.session['name'] = request.POST['name']  # more on session below
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        
        return redirect("/result")
    else:
        return redirect("/")


def result(request):
    print('########## inside result ##########')
    return render(request, 'survey_form/result.html')

def reset(request):
    request.session.clear()
    return redirect('/')