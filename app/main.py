# Contains the main Flask routes and logic 
#from flask import Flask, render_template, request, redirect
#from app import app, database


from flask import Flask, render_template, request, redirect
from app import app, database



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
def user(user_id):
    if request.method == 'POST':
        name_id = int(request.form['name_id'])
        response = request.form['response']
        database.record_response(user_id, name_id, response)
        return redirect(f'/user/{user_id}')
    else:
        names = database.get_names()
        return render_template('user.html', user_id=user_id, names=names)

@app.route('/results')
def results():
    common_names = database.get_common_names()
    return render_template('results.html', common_names=common_names)

if __name__ == '__main__':
    app.run(debug=True)
