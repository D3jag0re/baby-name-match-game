# Contains the main Flask routes and logic 
#from flask import Flask, render_template, request, redirect
#from app import app, database

from flask import Flask, render_template, request, redirect, url_for
from app import app, database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
def user(user_id):
    if request.method == 'POST':
        names = database.get_names()
        for name in names:
            name_id = name[0]
            response = request.form.get(f'response_{name_id}')
            if response:
                database.record_response(user_id, name_id, response)

        if user_id == 1:
            return redirect(url_for('submitted', user_id=user_id + 1))
        else:
            return redirect(url_for('submitted', user_id=0))

    else:
        names = database.get_names()
        return render_template('user.html', user_id=user_id, names=names)

@app.route('/submitted/<int:user_id>')
def submitted(user_id):
    if user_id == 0:
        return render_template('submitted.html', next_step='results')
    else:
        return render_template('submitted.html', next_step=f'/user/{user_id}')

@app.route('/results')
def results():
    common_names = database.get_common_names()
    return render_template('results.html', common_names=common_names)

@app.route('/reset', methods=['POST'])
def reset():
    database.reset_db()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

