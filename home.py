import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
  return "Welcome to Jian's world!"

@app.route('/xiaomo')
def xiaomo():
  return render_template("home.html")
