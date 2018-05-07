# basic validation
from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="thisIsmysecret2323232"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["post"])
def process():
    #name validation here
    if len(request.form['name']) < 1:
        #display val error
        flash('name cannot be empty')
    else:
        #display success
        flash(f"success! your name is {request.form['name']} !!!")
          
    # email validation
    if len(request.form['email']) < 1:
        flash('email cannot be blank!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('invald email address!')
    else:
        flash('success!')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    
