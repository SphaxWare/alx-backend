#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template
from flask import request, g
from flask_babel import Babel

app = Flask(__name__)

users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


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
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(id):
    """user login"""
    return users.get(int(id), None)


@app.before_request
def before_request():
    """
    should use get_user to find a user if any, and
    set it as a global on flask.g.user
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


if __name__ == '__main__':
    app.run()
