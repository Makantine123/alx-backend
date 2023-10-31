#!/usr/bin/env python3
"""basic Flask app module"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """Config class"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.url_map.strict_slashes = False


def get_user(user_id):
    """Returns user dictionary or None if ID cannot be found"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Finds user if any and set it as a global on flask.g.user"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale():
    """Get best fit local language"""
    return request.args.get(
        'locale', request.accept_languages.best_match(app.config['LANGUAGES']))


@app.route('/')
def index():
    """Welcome page"""
    home_title = _('home_title')
    home_header = _('home_header')
    return render_template('4-index.html',
                           home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run(debug=True)
