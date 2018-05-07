from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='thisisjustagame123123'
print('\n', '= = = = server start = = = =')


@app.route('/')
def index():
    print('--- in index ---')
    magicNum = random.randrange(0,101) # random num 0-100
    # create session if non existant
    if 'magicNum' not in session:
        session['magicNum'] = magicNum
    print(session)
    print('(╯°□°）╯ ',session['magicNum'])
    #if box doesnt exit pass, otherwise make it red as default
    if 'box' in session:
        pass
    else:
        session['box'] = 'box'

    # session['box'] = ''
    return render_template('index.html', numHTML=session['magicNum'])

@app.route('/submitted', methods=['POST'])
def submitted():
    valueshow = ''
    print(' # # #  buton pressed - got form # # # ')
    print(' this is the request.form ===> ',request.form)
    print(" printing request.form['textinput'] ====>> ", request.form['textinput'])
    # session['box'] = 'box'
    # set input value from form
    inputval = int(request.form['textinput'])
    
    # check if value entered is high or low
    if inputval > int(session['magicNum']):
        print(' > > > > > > > too high')
        session['valueshow'] = 'too high'
        session['box'] = 'box'
    if inputval < int(session['magicNum']):
        print(' < < < < < < < too low')
        session['valueshow'] = 'too low'
        session['box'] = 'box'
    
    # check if win condition
    if inputval == int(session['magicNum']):
        print(' YES THE NUMS MATCH!!!!!!!!! WOOHOO !!!!!')
        session['valueshow'] = 'YOU WON (╯°□°）╯ !!!!'
        session['box'] = 'boxwin'
        print(' AFTER BOXWIN @#@#@#@#@#@#@#@#@# #@ #@ @@# @# @ ')
        # session.clear()
    else:
        print('no match :( :( :( :( ')
    return redirect('/')

@app.route('/reset')
def reset():
    # session.pop['magicNum']
    session.clear()
    print(session)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)