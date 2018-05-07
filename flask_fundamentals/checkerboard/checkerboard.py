from flask import Flask, render_template
app = Flask(__name__)

print('\n','--'*5,' server start ','--'*5)

@app.route('/')
def index():
    return render_template('index.html',x=8 ,y=8)

@app.route('/<x>/<y>')
def xy(x,y):
    return render_template('index.html',x=int(x),y=int(y))

if __name__=='__main__':
    app.run(debug=True)
