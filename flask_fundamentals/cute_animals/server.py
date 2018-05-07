# cute animals
from flask import Flask, render_template
app = Flask(__name__)

print('\n', '--- server start ---')

@app.route('/')
def index():
    return render_template('index.html', numhtml=10)


@app.route('/<x>/')
def animalshow(x):
    return render_template('index.html', numhtml=int(x))

@app.route('/danger/')
def dangerpage():
    print('# # # # # user accessed DANGER ZONE # # # # #')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)