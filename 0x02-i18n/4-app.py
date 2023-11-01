#!/usr/bin/env python3
"""basic Flask app module"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config class"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale():
    """Get best fit local language"""
    locale = request.args.get('locale', '')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Welcome page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0', debug=True)
