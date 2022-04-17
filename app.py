#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_page():
    """Says Salute"""
    return "Salut Evanz!"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
