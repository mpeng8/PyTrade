from flask import render_template, url_for, redirect, session, abort, request, flash, g
from app import app
import re
from app import db
from app.models import User, Stock
import pandas as pd
import json


@app.route('/')

#############################################################################################################
@app.route('/index')
def index():
    if not session.get('logged_in'):
        return render_template('index.html')
    return dashboard()

@app.route('/timeout')
def timeout():
    error = "TIME OUT, please log in again."
    return render_template('login.html', error = error)

############################################################################################################
# login Signup functions
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
    print type(q_user)
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
################################################################################################
# page direction functions
@app.route("/dashboard")
def dashboard():
    if not session.get('username'):
        return redirect(url_for('timeout'))
    return render_template('dashboard.html')

@app.route("/admindashboard")
def admindashboard():
    if not session.get('username'):
        return redirect(url_for('timeout'))

    return render_template('admindashboard.html')

@app.route("/about")
def about():
    if not session.get('username'):
        return redirect(url_for('timeout'))

    return render_template('blank.html')

##############################################################################################
#stock list functions
@app.route("/stocklist", methods = ['GET', 'POST'])
def stocklist():
    if not session.get('username'):
        return redirect(url_for('timeout'))

    return render_template('stocklist.html')

@app.route("/stockinfo", methods = ['GET', 'POST'])
def stockinfo():
    if not session.get('username'):
        return redirect(url_for('timeout'))

    post = "empty";
    if(request.method == "POST"):
        post = request.form["stockName"];
        stockID = post.split(':', 1 )[0];
        post = post.split(':',1)[1];

    return render_template('stockinfo.html', stockName=post, stockID = stockID)

@app.route('/searchStock', methods = ['GET', 'POST'])
def searchStock():
    if not session.get('username'):
        return redirect(url_for('timeout'))

    post = request.form["stockName"];
    if (not post):
        print "aaa"
    stockID = post.split(':', 1 )[0];
    post = post.split(':',1)[1];

    return render_template('stockinfo.html', stockName=post, stockID = stockID)

#############################################################################################################

#Social network functions

@app.route("/myprofile")
def myprofile():
    if not session.get('username'):
        return redirect(url_for('timeout'))
    q_user = User.query.filter(User.username == session['username']).first()
    return render_template('profile.html', me = q_user, cur_user = q_user)

@app.route("/followers", methods = ['GET', 'POST'])
def followerslist():
    if not session.get('username'):
        return redirect(url_for('timeout'))

    q_user = User.query.filter(User.username == session['username']).first()

    followed = q_user.followed.all()
    follower = q_user.followers.all()

    return render_template('follower.html', follower = follower, followed = followed)

@app.route("/follow/<user>")
def follow(user):
    if not session.get('username'):
        return redirect(url_for('timeout'))
    q_user = User.query.filter(User.username == session['username']).first()
    q2_user = User.query.filter(User.username == user).first()
    q_user.follow(q2_user)
    db.session.commit()
    return redirect(url_for('followerslist'))

@app.route("/unfollow/<user>")
def unfollow(user):
    if not session.get('username'):
        return redirect(url_for('timeout'))
    q_user = User.query.filter(User.username == session['username']).first()
    q2_user = User.query.filter(User.username == user).first()
    q_user.unfollow(q2_user)
    db.session.commit()
    return redirect(url_for('followerslist'))

@app.route("/lookup_profile", methods=['POST','GET'])
def lookup_profile():
    if not session.get('username'):
        return redirect(url_for('timeout'))
    user = request.form['name']
    q_user = User.query.filter(User.username == session['username']).first()
    q2_user = User.query.filter(User.username == user).first()
    return render_template('profile.html', me = q_user, cur_user = q2_user)

# error handling
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
