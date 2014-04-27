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
  delta_t = datetime.datetime.now(pytz.timezone('Asia/Hong_Kong'))-\
      datetime.datetime(2014, 2, 23, 21, 31, 48, tzinfo=pytz.timezone('Asia/Hong_Kong'))
  day = delta_t.days
  hour = delta_t.seconds/3600
  minute = delta_t.seconds%3600/60
  second = delta_t.seconds%3600%60
  t_till_now = {'day':day, 'hour': hour, 'minute':minute, 'second':second}
  return render_template("home.html",t=t_till_now)
