from flask import Flask, session, render_template, redirect, request, flash
from flask_bcrypt import Bcrypt
import re
from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key='Fg5g45wg5wgw4545ufghfgfftyt5'

mysql = connectToMySQL('wall-db')
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

    errorValidation = False

    # -------------- FIRST NAME
    if request.form['first_name'] == '':
        print('@@@@@@ First name is empty')
        flash('first name cannot be empty', 'fname')
        errorValidation = True
    if len(request.form['first_name']) < 2:
        print('@@@@@@@@@ first name is LESS than 2 char') 
        flash('First name must have AT LEAST 2 letters', 'fname')
        errorValidation = True
    if request.form['first_name'].isalpha() == False:
        print('@@@@@@@@@@ first name is not a string')
        flash('First name must contain ONLY letters', 'fname')
        errorValidation = True

    # ------------ LAST NAME
    if request.form['last_name'] == '':
        print('@@@@@@ LAST name is empty')
        flash('Last name cannot be empty', 'lname')
        errorValidation = True
    if len(request.form['last_name']) < 2:
        print('@@@@@@@@@ LAST name is LESS than 2 char') 
        flash('Last name must have AT LEAST 2 letters', 'lname')
        errorValidation = True
    if request.form['last_name'].isalpha() == False:
        print('@@@@@@@@@@ LAST name is not a string')
        flash('Last name must contain ONLY letters', 'lname')
        errorValidation = True

    #-------------- EMAIL
    if len(request.form['email']) < 1:
        flash('email cannot be blank!', 'email')
        errorValidation = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('invalid email address!', 'email')
        errorValidation = True

    # ========= check what email we are getting
    query_email = "SELECT email FROM users WHERE email='{}';".format(request.form['email'])
    print(query_email)
    email_check = mysql.query_db(query_email)
    print('("@@@@@@@@@@@@@@@@@@@@  email_check check is: ', email_check)
    #============ EMAILcheck if in DB ===============
    if len(email_check) > 0:
        print('@@@@@@@@@@@@@@@@@@@@  MATCH -- email_check check is: ', email_check[0])
        flash('email already in use - cannot use this email !!!')
        errorValidation = True
    else:
        print('@@@@@@@@@@@@@@@@@@@@ NO match -- ')
    print("@@@@@@@@@@@@@@@@@@@@ DONE email check")
    # ----------------- PASSWORD validation

    # ################## PASSWORD validation #####################################
    if len(request.form['password1']) <1:
        print('@@@@@@@@@@@@@@@ PW1 is empty')
        flash('PW1 is empty')
        errorValidation = True
    if request.form['password1'] != request.form['password2']:
        flash('@@@@@@@@ pw do not match!')
        print('@@@@@@@@ PW DO NOT MATCH')
        errorValidation = True
        #if pw match...
    if request.form['password1'] == request.form['password2']:
        print('@@@@@@@@@ PASSWORDS MATCH!!! @@@@@ now hash pw1 and store it!')
        # ...CREATE HASH
        # pw_hash = bcrypt.generate_password_hash(request.form['password'])  
        # print('############# pw_hash =', pw_hash) 
        # query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password_hash)s);"
        # # put the pw_hash in our data dictionary, NOT the password the user providedcopy
        # data = { "username" : request.form['username'],"password_hash" : pw_hash }
        # mysql.query_db(query, data)
    # never render on a post, always redirect!

    # ====== retain sessions for FIRST, LAST, EMAIL in case of error


    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    # =-=-=-=-=-=- FINAL VALIDATION =-=-=---=-=-=-=
    if errorValidation == False:
        if request.form['password1'] == request.form['password2']:
            print('@@@@@@@@@ PASSWORDS MATCH!!! @@@@@ now hash pw1 and store it!')
             # if pw match CREATE HASH
            pw_hash = bcrypt.generate_password_hash(request.form['password1'])  
            print('############# pw_hash =', pw_hash) 
            query = "INSERT INTO users (first_name, last_name, email, created_at, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), %(password_hash)s);"
            # put the pw_hash in our data dictionary, NOT the password the user providedcopy
            # insert users & PW into DB
            data = { 'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'created_at': '', "password_hash" : pw_hash }
            mysql.query_db(query, data)
            print('@@@@@@@@@@@@@ passed all validations @@@@')
        return redirect('/wall')

    return redirect('/')
    

@app.route('/login', methods=['post'])
def login():
    print('\n','----------- inside /login')
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = { "email" : request.form["email"] }
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password3']):
            session['userid'] = result[0]['id']
            
            # this retrieves the first name that matches the email given from post:
            query_fname = "SELECT first_name FROM users WHERE email='{}';".format(request.form['email'])
            print(query_fname)
            fname_check = mysql.query_db(query_fname)
            # fname_check[0]['first_name'] -> gets the first name from 0 index key 'first_name'
            print('("@@@@@@@@@@@@@@@@@@@@  Fname_check check is: ', fname_check[0]['first_name'])

            session['first_name'] = fname_check[0]['first_name']

            
            # session['name'] = name
            return redirect('/wall')
        flash("You could not be logged in")
        return redirect("/")
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
