from flask import Flask, session, render_template, redirect, request, flash
from flask_bcrypt import Bcrypt
import re
from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key='Fg5g45wg5wgw5g45ytjuy5terytu88u8ufghfgfftyt5'

mysql = connectToMySQL('email-valid-db')
print('\n','= = = server start = = = server.py ')


@app.route('/')
def index():
    # return render_template('index.html', emailsHTML = all_emails)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def emailVaild():
    print('\n= = = = GOT POST INFO = = = = ')
    print(request.form)
    print('= = = = END OF POST INFO = = = =')

    if 'email' not in session:
        session['email'] = ''
    # flag
    validationError = False

     # E-mail
    if len(request.form['email']) < 1:
        flash('email cannot be blank!')
        validationError = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('invalid email address!')
        validationError = True
    query_email = "SELECT * FROM emails WHERE email='{}';".format(request.form['email'])
    print(query_email)
    email_check = mysql.query_db(query_email)
    print('("@@@@@@@@@@@@@@@@@@@@  email_check check is: ', email_check)

    if len(email_check) > 0:
        print('@@@@@@@@@@@@@@@@@@@@  MATCH -- email_check check is: ', email_check[0])
        flash('email already in use!!!')
        validationError = True
    else:
        print('@@@@@@@@@@@@@@@@@@@@ NO match -- ')

    print("@@@@@@@@@@@@@@@@@@@@ DONE")

        # FINAL CHECK
    if validationError == False:
        flash('all ok!!')
        print(' ! ! ! all checks ok ! ! ! ')
        query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW()); "
        data = {'email': request.form['email'] }
        mysql.query_db(query, data)
    else:
        return redirect('/')
    session['email'] = request.form['email']
    return redirect('/success')

@app.route('/success')
def success():
    all_emails = mysql.query_db("SELECT * FROM emails")
    print('\n','-=-=-=-=-=- show all emails from db -=-=-=-=-=-\n')
    print("Fetched all emails", all_emails,'\n')
    print('-=-=-=- end of show all emails form db -=-=-=-\n')
    return render_template('success.html', emails = all_emails)

@app.route('/delete', methods=['POST'])
def delete():
    print('\n DELETING entry  * * * * * * *')
    print(request.form['id'])
    query = "DELETE FROM emails WHERE id=%(id)s; "
    data = {'id': request.form['id'] }
    mysql.query_db(query, data)
    return redirect('/success')



if __name__ == "__main__":
    app.run(debug=True)