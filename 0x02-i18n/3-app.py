#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template
from flask import request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


babel = Babel(app)


@app.route('/')
def index():
    """index"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
