import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "Welcome to Jian's world!"

@app.route('/xiaomo')
def xiaomo():
  return '''Having you being my girl friend is the best honor and greatest luck\nWish you happy every day -- fighting for the future"
