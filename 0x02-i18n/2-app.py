#!/usr/bin/env python3
"""get locale"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


class Config(object):
    """config class for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False

@babel.localeselector
def get_locale():
    """function which is invoked for each
    request to select a language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """route for default page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
