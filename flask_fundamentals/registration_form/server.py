from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app=Flask(__name__)
app.secret_key='98ehfu9whguhfu99u3fbaazzz'
print('\n','= = = server start = = =')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    print('\n','-=-=-=- inside /process -=-=-=-=')

    # flag
    validationError = False

    # First Name
    if request.form['fname'] == '':
        flash('name cannot be blank')
        validationError = True
    if len(request.form['fname']) < 3:
        flash('name must have at least 3 letters')
        validationError = True
    if str(request.form['fname']).isdigit():
        flash('name cannot have any numbers!')
        validationError = True

    # Last name
    if request.form['lname'] == '':
        flash('Last name cannot be blank')
        validationError = True

    # E-mail
    if len(request.form['email']) < 1:
        flash('email cannot be blank!')
        validationError = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('invalid email address!')
        validationError = True

    # PASSWORD
    if len(request.form['password1']) < 1:
        flash('password cannot be blank!')
        validationError = True
    elif len(request.form['password1']) < 8:
        flash('password must be AT LEAST 6 characters long!')
        validationError = True
    if request.form['password1'] != request.form['password2']:
        flash('passwords do not match!')
        validationError = True

    # FINAL CHECK
    if validationError == False:
        flash('all ok!!')
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
