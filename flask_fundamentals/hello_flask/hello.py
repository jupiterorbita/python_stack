from flask import Flask, render_template
app = Flask(__name__)

print('printing : __name__ --> ', __name__)

@app.route('/')
def hello_world():
    # return 'Hello World@@@@@!'
    return render_template('index.html',name='jay')

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "hello "+name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username,id):
    print(username)
    print(id)
    return "username: "+username+", id: "+id

@app.route('/some_route')
def some_function_name():
    print('some function')
    return 'some_function_name returned'


app.run(debug=True) 
