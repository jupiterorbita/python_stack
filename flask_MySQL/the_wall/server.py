from flask import Flask, session, render_template, redirect, request, flash
from flask_bcrypt import Bcrypt
import re
# from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key='Fg5g45wg5wgw4545ufghfgfftyt5'

# mysql = connectToMySQL('wall_db')
print('\n','= = = server start = = = server.py ')

@app.route('/')
def index():
    # ======= session checks ==========
    # first name check session
    if 'first_name' not in session:
        session['first_name'] = ''
    # last name check session
    if 'last_name' not in session:
        session['last_name'] = ''
    # email check session
    if 'email' not in session:
        session['email'] = ''
    # pass vars to browser to remember values
    return render_template('index.html', temp_fname=session['first_name'], temp_lname=session['last_name'], temp_email=session['email'])

@app.route('/register', methods=['post'])
def register():
    print('\n','----------- inside /register')

    return redirect('/')
    

@app.route('/login', methods=['post'])
def login():
    print('\n','----------- inside /login')
    return redirect('/')
  
@app.route('/wall')
def wall():
    print('\n', '---------- inside /wall')
    return render_template('wall.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
