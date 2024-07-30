#!/usr/bin/env python3
"""
Flask app for demonstrating internationalization (i18n) with Flask-Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, get_locale
from pytz import timezone
from datetime import datetime



class Config:
    """
    Configuration class for Flask-Babel.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.init_app(app, locale_selector=get_locale)
def get_locale():
    """
    Selects the best match language from the request.

    Returns:
        str: Best matched language.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/', strict_slashes=False)
def index():
    """
    Landing route for the Flask application.

    Renders the `0-index.html` template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
