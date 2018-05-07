from flask import (Flask, render_template, redirect, request, session)
import random
app = Flask(__name__)
app.secret_key='abclalalala2323'
print('\n', '=== server start ===')

@app.route('/')
def index():
    print('--- in "/" route ---')
    # if 'farmGoldRnd' in session:      # init gold from farm
    #     pass
    # else: session['farmGoldRnd'] = 0
    print('session ->',session)
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    print('--- in "/process_money ---')
    print("printing request.form['building']", request.form['building'])
    if 'total_gold' not in session:
        session['total_gold'] = 0
    if 'msg' not in session:
        session['msg'] =''

    # farm
    if request.form['building'] == 'farm':
        session['farmGold'] = random.randrange(10,20)
        session['total_gold'] += session['farmGold']
        session['msg'] = "<p class=green> cool you got "+str(session['farmGold'])+" gold from farm </p>"+session['msg']
    
    # cave
    elif request.form['building'] == 'cave':
        session['caveGold'] = random.randrange(10,20)
        session['total_gold'] += session['caveGold']
        session['msg'] = "<p class=green> cool you got "+str(session['caveGold'])+" gold from cave </p>"+session['msg']
    
    # house
    elif request.form['building'] == 'house':
        session['houseGold'] = random.randrange(2,5)
        session['total_gold'] += session['houseGold']
        session['msg'] = "<p class=green> cool you got "+str(session['houseGold'])+" gold from HOUSE </p>"+session['msg']
    
    # casino
    elif request.form['building'] == 'casino':
        session['casinoGold'] = int(random.randrange(-50,50))
        # ! ! ! becuase its a -negative num we have to ADD it!!!
        if session['casinoGold'] < 0:
            session['total_gold'] += session['casinoGold']
            session['msg'] = "<p class=red> oh NO! you lost "+str(session['casinoGold'])+" gold from the casino</p>"+session['msg']
        elif session['casinoGold'] > 0:
            session['total_gold'] += session['casinoGold']
            session['msg'] = "<p class=green> LUCKY YOU! +"+str(session['casinoGold'])+" gold from the casino </p>"+session['msg']
    # else:
    #     pass
    return redirect('/')


@app.route('/reset')
def reset():
    print('--- RESETING ---')
    session.clear()
    # session.pop['gold']
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
