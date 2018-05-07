from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="343uhr32u4923g49u32h4"
print('\n','===== server start =====')

@app.route('/')
def index():
    if 'name' not in session:
        session['name']=''
    if 'description' not in session:
        session['description'] =''

    return render_template('index.html', name=session['name'], descr=session['description'])

@app.route('/forminfo', methods=['POST'])
def forminfo():
    print('\n')
    print(' = = = = got POST info = = = =')
    print(request.form)
    print(' = = = = end of POST info = = = = =')
    print('\n')
    session['name'] = request.form['name']
    session['description'] = request.form['description']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    
    validationErrors = False

    # name valid
    if len(request.form['name']) == 0:
        validationErrors = True
        flash('name cannot be empty!')
    elif len(request.form['name']) < 4:
        validationErrors = True
        flash('name must be more than 3 characters long')

    # description valid
    if len(session['description']) > 120:
        validationErrors = True
        flash('comments cannot exceed 120 characters :(')

    if validationErrors:
        return redirect('/')
    else:
        return redirect('/success')

@app.route('/success')
def success():
    return render_template('result.html')

@app.route('/reset')
def reset():
    print('\n')
    print(' = = = = session cleared = = = =')
    session.clear()
    print(' = = = = redirecting to "/"  = = = = =')
    print('\n')
    return redirect ('/')

@app.route('/danger/')
def danger():
    print('# # # # # # # # # # # # # # # DANGER ZONE')
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)
