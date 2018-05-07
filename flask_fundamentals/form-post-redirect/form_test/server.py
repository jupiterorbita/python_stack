from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"  # sets a secret key for security purpose

print('\n', '----- server start -----')


@app.route('/')
def index():
    if 'name' in session:
        print('name exists!')
    else:
        print("key 'name' DOES NOT exist")
    # session['cntr'] = session['name'] + 1
    return render_template('index.html')

# this route is for form submission
# we define which HTTP method is allowed by this route
@app.route('/users/', methods=['POST'])
def create_user():
    print('# # # GOT POST INFO # # #')
    print(request.form)
    # name = request.form['name']
    # email = request.form['email']
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')  


@app.route('/show')
def show_user():
  return render_template('user.html')
#   return render_template('user.html', name=session['name'], email=session['email'])


if __name__ == "__main__":
    app.run(debug=True)
