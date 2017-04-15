#!flask/bin/python
from app import app
from datetime import timedelta

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

app.permanent_session_lifetime = timedelta(seconds=600)
app.run(debug=True)
