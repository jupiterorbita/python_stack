from flask import Flask, render_template, request, redirect
app = Flask(__name__)

print('\n','===== server start =====')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def forminfo():
    print(' = = = = got POST info = = = =')
    print(request.form)
    print(' = = = = end of POST info = = = = =')
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    description = request.form['description']
    return render_template('/result.html', namehtml =name, locationhtml =location, languagehtml =language, decriptionhtml =description)

@app.route('/danger/')
def danger():
    print('# # # # # # # # # # # # # # # DANGER ZONE')
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)
