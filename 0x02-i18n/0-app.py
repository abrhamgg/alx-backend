#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """route for default page"""
    return render_template('0-index.html')
