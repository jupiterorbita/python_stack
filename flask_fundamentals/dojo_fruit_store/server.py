from flask import Flask, render_template, request, redirect
import os, math
app = Flask(__name__)  
imgFiles = os.listdir("static/img")


print('\n', '+_+_+_+_+ server start +_+_+_+_+')

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print('= = = = = = got POST info = = = = = =')
    print(request.form)
    print('= = = = = = end of POST info = = = = = =')
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html",imgFiles = imgFiles)

if __name__=="__main__":   
    app.run(debug=True)    