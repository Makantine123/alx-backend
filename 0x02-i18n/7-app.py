#!/usr/bin/env python3
"""basic Flask app module"""

from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


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


@babel.timezoneselector
def get_timezone():
    """Timezone selector"""
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    user = g.user
    if user and 'timezone' in user:
        user_timezone = user['timezone']
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """Returns user dictionary or None if ID cannot be found"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """Finds user if any and set it as a global on flask.g.user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Get best fit local language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    user = g.user
    if user and 'locale' in user:
        locale = user['locale']
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Welcome page"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(debug=True)
