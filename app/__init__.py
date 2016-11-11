from flask import Flask, request, render_template,session
from datetime import timedelta

app = Flask(__name__)
#set session time
app.permanent_session_lifetime = timedelta(seconds=180)

app.config.from_object('config')
from app import views
