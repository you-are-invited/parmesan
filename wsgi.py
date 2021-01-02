from flask import Flask, send_from_directory
from flask_wtf.csrf import CSRFProtect
import os
import secrets
import string


# create a random SECRET KEY
def create_secret_key(length):
    key = ""
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        key += secrets.choice(characters)
    return key


# Create app and load secret key
app = Flask(__name__)
app.config['SECRET_KEY'] = create_secret_key(64)

# initialize csrf protection
csrf = CSRFProtect()
csrf.init_app(app)

# import all views
import views


# serve static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
