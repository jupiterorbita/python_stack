from flask import Flask, session, request, redirect, render_template
import random
app=Flask(__name__)
app.secret_key="9824hfiuwenfiwenfoe"
print('\n','= = = starting server = = =')

@app.route('/')
def index():
    print('-=-=--=-=-=-= in index =-=-=-=-=-=- ')
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    print('\n','-=-=- in /process -=--=-=-')
    # print('form data ====> ', request.form)

    if 'total_gold' not in session:
        session['total_gold'] = 0
    if 'msg' not in session:
        session['msg'] = ''
    
    if request.form['building'] == 'farm':
        fgold = random.randrange(5,10)
        session['total_gold'] += fgold
        session['msg'] = "<p class='green'> you got "+str(fgold)+" gold from FARM</p>"+session['msg']

    if request.form['building'] == 'casino':
        cgold = random.randrange(-50,50)
        if cgold < 0:
            session['total_gold'] += cgold
            session['msg'] = "<p class='red'> you LOST "+str(cgold)+" gold from CASINO</p>"+session['msg']
        if cgold >= 0:
            session['total_gold'] += cgold
            session['msg'] = "<p class='green'> LUCKY *** you WON "+str(cgold)+" gold from CASINO</p>"+session['msg']
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)