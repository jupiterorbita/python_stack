from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= "Thisismysecretkey"

print('\n', '====== server start ======')

@app.route('/')
def index():
    print(' -=-=-=- printing inside index =-=-=-=-')
    print(session)
    if 'counter' in session:
        print('/////// sesion exists ///////')
        session['counter'] += 1
    else:
        print('$ $ $ $ $  no session, creating new session, conter=1')
        session['counter'] = 1
    print(session)
    # if request.form['action'] == 'plus2':
    #     session['counter'] += 2
    return render_template('index.html')

@app.route('/reload/')
def reload():
    print(' zzz...zzz... adding to counter +2 ')
    for counter in session:
        session['counter'] +=2
    return render_template('index.html')

@app.route('/destroy_session/')
def destroy():
    print('!!!!!!!!!! session destroyed !!!!!!!!!')
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

