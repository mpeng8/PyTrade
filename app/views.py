from flask import render_template, url_for, redirect,session,abort, request, flash
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    if not session.get('logged_in'):
    	return render_template('index.html')
    else:
	return render_template('dashboard.html')
    

@app.route('/login', methods = ['GET','POST'])
def login():
    return render_template('login.html')


@app.route('/auth', methods = ['POST'])
def userLogIn():
    error = None
    print(request.form['password'])
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        error = 'Invalid Credentials'
	return render_template('login.html', error = error)
    return index()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()
