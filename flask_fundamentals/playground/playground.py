from flask import Flask, render_template
app = Flask(__name__)

print('\n', '--- server start ---')


@app.route('/')
def index():
    # print('returing index -> ')
    return render_template('index.html', xhtml=3, colorhtml='blue')


@app.route('/play/<num>/')
def level2(num):
    return render_template('index.html', xhtml=int(num), colorhtml='blue')


@app.route('/play/<num>/<color>/')
def level3(num, color):
    return render_template('index.html', xhtml=int(num), colorhtml=color)


if __name__ == "__main__":
    app.run(debug=True)
