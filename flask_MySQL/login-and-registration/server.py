from flask import Flask, session, render_template, redirect, request, flash
from flask_bcrypt import Bcrypt
import re
from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key='Fg5g45wg5wgw5g4656rf5ytjuy5terytu88u8ufghfgfftyt5'

mysql = connectToMySQL('login_registration_db')
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

@app.route('/register', methods=['POST'])
def register():
    print('\n= = = = GOT POST INFO = = = = ')
    print(request.form)
    print('= = = = END OF POST INFO = = = =')
    

    # ========== validation checks ===========
    # flag set
    validationError = False
    passValidationError = False

    # --------------- FIRST NAME validation
    if request.form['first_name'] == '':
        print('@@@@@@@ FIRST is empty ----')
        flash('First name cannot be empty!')
        validationError = True
    if len(request.form['first_name']) < 2:
        print('@@@@@@@ FIRST is less than 2 chars ---') 
        flash('First name must be more than 2 letters!')
        validationError = True
    if request.form['first_name'].isalpha() == False:
        print('@@@@@@@ FIRST is not a string -----') 
        flash('First name must contain ONLY LETTERS')
        validationError = True

    # --------------- LAST NAME validation
    if request.form['last_name'] == '':
        print('@@@@@@@ LAST name is empty ----')
        flash('Last name cannot be empty!')
        validationError = True
    if len(request.form['last_name']) < 2:
        print('@@@@@@@ LAST name is less than 2 chars ---') 
        flash('Last name must be more than 2 letters!')
        validationError = True
    if request.form['last_name'].isalpha() == False:
        print('@@@@@@@ LAST is not a string -----') 
        flash('Last name must contain ONLY LETTERS')
        validationError = True

    # ---------------- EMAIL validation
    if len(request.form['email']) < 1:
        flash('email cannot be blank!')
        validationError = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('invalid email address!')
        validationError = True
    # ========= check what email we are getting
    query_email = "SELECT email FROM users WHERE email='{}';".format(request.form['email'])
    print(query_email)
    email_check = mysql.query_db(query_email)
    print('("@@@@@@@@@@@@@@@@@@@@  email_check check is: ', email_check)
    #============ EMAILcheck if in DB ===============
    if len(email_check) > 0:
        print('@@@@@@@@@@@@@@@@@@@@  MATCH -- email_check check is: ', email_check[0])
        flash('email already in use - cannot use this email !!!')
        validationError = True
    else:
        print('@@@@@@@@@@@@@@@@@@@@ NO match -- ')
    print("@@@@@@@@@@@@@@@@@@@@ DONE email check")
    # ----------------- PASSWORD validation

    # ################## PASSWORD validation #####################################
    if len(request.form['password1']) <1:
        print('@@@@@@@@@@@@@@@ PW1 is empty')
        flash('PW1 is empty')
        validationError = True
    if request.form['password1'] != request.form['password2']:
        flash('@@@@@@@@ pw do not match!')
        print('@@@@@@@@ PW DO NOT MATCH')
        validationError = True
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
    if validationError == False:
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
        return redirect('/success')
    
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
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
            return redirect('/success')
        flash("You could not be logged in")
        return redirect("/")


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
