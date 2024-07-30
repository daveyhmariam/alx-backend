#!/usr/bin/env python3
"""
Flask app for demonstrating internationalization (i18n) with Flask-Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
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


@app.route('/', strict_slashes=False)
def index():
    """
    Landing route for the Flask application.

    Renders the `0-index.html` template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("0-index.html")

@babel.localeselector
def get_locale():
    request.accept_languages.best_match(app.config("LANGUAGES"))
if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
