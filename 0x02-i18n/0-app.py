#!/usr/bin/env python3
"""Flask app
"""
from flask import Flask, route, render_template

app = Flask(__name__)


@route('/', strict_slashes=False)
def index():
    """
    landing route
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
