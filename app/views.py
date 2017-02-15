from flask import render_template, url_for, redirect, session, abort, request, flash
from app import app
import re
from app import db
from app.models import User, Stock
import pandas as pd
import json


@app.route('/')

@app.route('/index')
def index():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return dashboard()

@app.route('/admin', methods = ['GET','POST'])
def adminlogin():
    return render_template('adminlogin.html')

def admin():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('admindashboard.html')


@app.route('/login', methods = ['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/auth', methods = ['POST'])
def userLogIn():
    error = None
    un = request.form['username']
    q_user = User.query.filter(User.username == un).first()

    if q_user == None:
        error = 'User not existed.'
    elif request.form['password'] == q_user.password:
        session['logged_in'] = True
        session['username'] = request.form['username']
    else:
        error = 'Invalid Credentials'
    if error != None:
       return render_template('login.html', error = error)
    return index()

@app.route('/auth2', methods = ['POST'])
def adminLogIn():
    error = None
    print(request.form['password'])
    if request.form['password'] == 'password' and request.form['username'] == 'admin2':
        session['logged_in'] = True
        session['username'] = request.form['username']
    else:
        error = 'Invalid Credentials'
    return render_template('adminlogin.html', error = error)
    return admin()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['username'] = None
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
    elif not re.match("[^@]+@[^@]+\.[^@]+",request.form['email']):
        error = 'Email is not valid'
    elif not request.form['email']:
        error = 'Email is blank'
    elif not request.form['password']:
        error = 'Password is blank'
    elif not (len(request.form['password']) >= 6 and len(request.form['password']) <= 30):
        error = len(request.form['password']),'Password length should between 6 and 30 symbols.'
    elif not request.form['re-password']:
        error = 'Please re-enter the password'
    else:
        # sign up successfully
        # do we need to make a pop up window or message?
        # or we can directly login to the account?
        u = User(request.form['username'], request.form['password'], request.form['email'])
        #session['logged_in'] = True

        print "Account create successfully.!"
        try:
            db.session.add(u)
            db.session.commit()
            db.session.close()
        except:
            error = 'Account creation failed.'
            db.session.rollback()
            return render_template('signup.html', error= error)

        return index()

    return render_template('signup.html', error= error)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/admindashboard")
def admindashboard():
    return render_template('admindashboard.html')

@app.route("/about")
def about():
    return render_template('blank.html')

@app.route("/stocklist", methods = ['GET', 'POST'])
def stocklist():
    return render_template('stocklist.html')

@app.route("/industrynews")
def industrynews():
    return render_template('industrynews.html')

@app.route("/stockinfo", methods = ['GET', 'POST'])
def stockinfo():
    post = "empty";
    if(request.method == "POST"):
        post = request.form["stockName"];
        stockID = post.split(':', 1 )[0];
        post = post.split(':',1)[1];

    return render_template('stockinfo.html', stockName=post, stockID = stockID)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
