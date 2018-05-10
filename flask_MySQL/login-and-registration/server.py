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
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    print('\n= = = = GOT POST INFO = = = = ')
    print(request.form)
    print('= = = = END OF POST INFO = = = =')
    # ======= session checks ==========
    # first name check session
    if 'fist_name' not in session:
        session['first_name'] = ''
    # last name check session
    if 'last_name' not in session:
        session['last_name'] = ''
    # email check session
    if 'email' not in session:
        session['email'] = ''

    # ========== validation checks ===========
    # flag set
    validationError = False
    # --------------- first name validation
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
    # --------------- last name validation
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
    # ---------------- email validation
    if len(request.form['email']) < 1:
        flash('email cannot be blank!')
        validationError = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('invalid email address!')
        validationError = True
    query_email = "SELECT email FROM users WHERE email='{}';".format(request.form['email'])
    print(query_email)
    email_check = mysql.query_db(query_email)
    print('("@@@@@@@@@@@@@@@@@@@@  email_check check is: ', email_check)

    if len(email_check) > 0:
        print('@@@@@@@@@@@@@@@@@@@@  MATCH -- email_check check is: ', email_check[0])
        flash('email already in use - cannot use this email !!!')
        validationError = True
    else:
        print('@@@@@@@@@@@@@@@@@@@@ NO match -- ')
    print("@@@@@@@@@@@@@@@@@@@@ DONE email check")

    # ################### pw validation
    # pw_hash = bcrypt.generate_password_hash(request.form['password'])  
    # print('############# pw_hash =', pw_hash) 

    # =-=-=-=-=-=- FINAL VALIDATION =-=-=---=-=-=-=
    if validationError == False:
        print('@@@@@@@@@@@@@ passed all validations @@@@')
        query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW()); "
        data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'created_at': '' }
        mysql.query_db(query, data)


    return redirect('/')


@app.route('/login', methods=['post'])
def login():
    return render_template('success.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
