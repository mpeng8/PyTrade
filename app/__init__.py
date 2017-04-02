from flask import Flask, request, render_template,session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)
#set session time
app.permanent_session_lifetime = timedelta(seconds=180)
app.config.from_object('config')


#we turn on the Flask-SQLAlchemy event system (and disable the warning)
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)

from app import views, models
