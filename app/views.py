"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from forms import *

###
# Routing for your application.
###
@app.route('/')
def home():
    """Render profile page"""
    return render_template('profile.html')
    
@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    """Render website's profile page."""
    if request.method == 'POST':
        # Accept profile details
        firstname = request.form['fistname']
        lastname = request.form['lastname']
        age = request.form['age']
        biography = request.form['biography']
        
        flash('Profile Added', 'success')
        next = request.args.get('next')
        return redirect(url_for('profile'))
    else:
        flash('There was an error! lets try again', 'oops')

    return render_template('profile.html')

@app.route('/profiles/', methods= ['GET', 'POST'])
def profiles():
    """Render the website's profiles page."""
    return render_template('profiles.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
