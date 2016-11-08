from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    print(url_for('static', filename='style.css'));
    return render_template('index.html')
