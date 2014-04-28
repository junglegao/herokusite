import os
from flask import Flask
from flask import render_template
import datetime
import pytz

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def home():
  return "Welcome to Jian's world!"

@app.route('/xiaomo')
def xiaomo():
  return render_template("home.html")
