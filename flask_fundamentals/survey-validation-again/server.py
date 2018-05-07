from flask import Flask, session, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="iu4hui43btiu34btu43itb34"
print('\n','=== server start ===')

@app.route('/')
def index():
    if 'name' not in session:
        session['name'] = ''
    if 'description' not in session:
        session['description'] = ''

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print('\n','--- in /process ---')
    print(f'printing request.form {request.form} --end')
    # return redirect('/')

    validationError = False

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    # session['gender'] = request.form['gender']
    session['description'] = request.form['description']

    # name check
    if len(session['name']) == 0:
        print('name == 0')
        flash('name cannot be empty!')
        validationError = True
    if len(session['name']) < 3:
        print('name < 3')
        flash('name must be 3+ letters long')
        validationError = True

    # textbox check
    if len(session['description']) > 120:
        print('description > 120')
        flash('comments must be less than 120 letters!')
        validationError = True
    
    if validationError == True:
        return redirect('/')
    else: 
        return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
