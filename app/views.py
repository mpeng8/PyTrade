from flask import render_template, url_for, redirect,session,abort, request, flash
from app import app
from .forms import LoginForm
import re
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
        session['username'] = request.form['username']
    else:
        error = 'Invalid Credentials'
	return render_template('login.html', error = error)
    return index()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

@app.route('/signup', methods = ['GET','POST'])
def signup():
    return render_template('signup.html')

@app.route('/aftersignup', methods = ['GET', 'POST'])
def userSignup():
    error = None
    print(request.form['username'])
    print(request.form['email'])
    print(request.form['password'])
    print(request.form['re-password'])
    if request.form['password'] != request.form['re-password']:
        error = 'Two unequal password.'
    elif not re.match("^[a-zA-Z0-9_#@!]*$",request.form['username']):
        error = 'Invalid characters for username'
        #elif reques.form['email'] exists in database
        #error = 'This email has already connect to an account'
    elif not request.form['username']:
        error = 'Username is blank'
    elif not request.form['email']:
        error = 'Email is blank'
    elif not request.form['password']:
        error = 'Password is blank'
    elif not request.form['re-password']:
        error = 'Please re-enter the password'
    else:
        # sign up successfully
        # do we need to make a pop up window or message?
        # or we can directly login to the account?
        session['logged_in'] = True
        return index()
    return render_template('signup.html', error= error)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/about")
def about():
    return render_template('blank.html')


