from flask import Flask, session, render_template, redirect, request, flash
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key='Fg5g45wg5wgw5g45ytjuy5terytuftyt5'

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('friends')
print('\n','= = = server start server.py = = =')

# now, we may invoke the query_db method
# print('-=-=-=-=-=- show all friends from db -=-=-=-=-=-\n', mysql.query_db("SELECT * FROM friends;"))
# print('-=-=-=- end of show all friends form db -=-=-=-\n')

@app.route('/')
def index():
    # all_friends = mysql.query_db("SELECT * FROM friends")
    all_friends = mysql.query_db("SELECT first_name, last_name, occupation FROM friends")
    print('\n','-=-=-=-=-=- show all friends from db -=-=-=-=-=-\n')
    print("Fetched all friends", all_friends,'\n')
    print('-=-=-=- end of show all friends form db -=-=-=-\n')

    if 'fname' not in session:
        session['fname'] = ''
    if 'lname' not in session:
        session['lname'] = ''
    if 'occup' not in session:
        session['occup'] = ''

    return render_template('index.html', friends = all_friends)



@app.route('/create_friend', methods=['POST'])
def create_friend():
    print('\n= = = = GOT POST INFO = = = = ')
    print(request.form)
    print('= = = = END OF POST INFO = = = =')

    # validationError = False
    # # first name check
    # if len(session['first_name']) == 0:
    #     flash('name cannot be empty!')
    #     validationError = True
    # if len(session['first_name']) < 3:
    #     flash('name must have AT LEAST 4 letters')
    #     validationError = True
    # # last name check
    # if len(session['last_name']) == 0:
    #     flash('Last Name cannot be empty!')
    #     validationError = True
    # if len(session['last_name']) < 3:
    #     flash('Last Name must have AT LEAST 4 letters')
    #     validationError = True
    # # occupation check
    # if len(session['occupation']) ==0:
    #     flash('Please fill in an occupation')
    #     validationError = True
    # if len(session['occupation']) < 3:
    #     flash('An occupation should have AT least 4 letters')
    #     validationError = True

    # if validationError = True:
    #     return redirect('/')
    # else:
    #     return redirect('/')


    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW()); "
    data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'occupation': request.form['occupation']}
    mysql.query_db(query, data)
    # AFTER THIS MAKE SESSION TO DISPLAY TO USER !!!
    


    

    # session['fname'] = data.first_name
    session['fname'] = request.form['first_name']
    session['lname'] = request.form['last_name']
    session['occup'] = request.form['occupation']


    # session['fname'] = request.form['first_name']
    # session['lname'] = request.form['last_name']
    # session['occup'] = request.form['occupation']

    return redirect('/')











if __name__ == "__main__":
    app.run(debug=True)