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

app = Flask(__name__)

# routing and controllers
# =======================

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

