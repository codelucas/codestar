# -*- coding: utf-8 -*-
"""
    CodeStar initial code.
    Please use 4 space indenting. No tabs!
"""
__author__ = 'Lucas Ou-Yang, Jason Tanner'
__date__ = 'November 2nd, 2013'
__version__ = '0.0.1'

# Imports
from flask import Flask
from flask import render_template
#from flask.ext.scss import Scss


app = Flask(__name__)
#Scss(app)

# routing and controllers
# =======================

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html');

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html');

@app.route('/user')
def user():
    return render_template('user.html');

if __name__ == '__main__':
    app.run(debug=True)

