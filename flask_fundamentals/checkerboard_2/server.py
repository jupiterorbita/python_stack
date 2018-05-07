from flask import Flask, render_template
app = Flask(__name__)

print('\n', '--- server start ---')


@app.route('/')
def board():
    return render_template('index.html')


app.run(debug=True)
