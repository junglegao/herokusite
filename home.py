import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "Welcome to Jian's world!"
