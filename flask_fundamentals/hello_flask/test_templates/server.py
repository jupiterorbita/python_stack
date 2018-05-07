from flask import Flask, render_template
app = Flask(__name__)
print('\n')
print('-------- server start -------')

@app.route('/')
def index():
    return render_template('index.html', phrase='hello world', times=5)

if __name__=='__main__':
    app.run(debug=True)
# hi :)