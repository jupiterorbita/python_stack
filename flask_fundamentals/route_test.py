from flask import flask
app = Flask(__name__)

print(__name__)

@app.route('/')