# Create a server file that generates 5 different http responses for the following 5 url requests:

# localhost:5000 - have it say "Hello World!" - Hint: If you have only one route that your server is listening for, it must be your root route ("/")
# localhost:5000/dojo - have it say "Dojo!"
# localhost:5000/say/flask - have it say "Hi Flask"
# localhost:5000/say/michael - have it say "Hi Michael" (have this be handled by the same route function as #3)
# localhost:5000/say/john - have it say "Hi John!" (have this be handled by the same route function as #3)
# localhost:5000/repeat/35/hello - have it say "hello" 35 times! - You will need to convert a string "35" to an integer 35.  To do this use int().  For example int("35") returns 35
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times! (have this be handled by the same route function as #6)


from flask import Flask
app=Flask(__name__)

print('\n\n', '_-'*10,'server start understanding_routing.py')

@app.route('/')
def hello_world():
    print('--PRINT-- default "/" will return hello world')
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    print('--PRINT-- will return "Dojo!"')
    return 'Dojo!'

@app.route('/say/flask')
def hiflask():
    print('hi flask from terminal')
    return 'hi Flask!'

@app.route('/say/michael')
def himichael():
    return 'hi Michael!'

@app.route('/repeat/<num>/hello')
def repeatnum(num):
    num = int(num)
    return 'hello '*num

@app.route('/repeat/<num>/<name>')
def repeat_all(num,name):
    num = int(num)
    return name * num





app.run(debug=True)