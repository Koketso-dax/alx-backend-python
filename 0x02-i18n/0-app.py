#!/usr/bin/env python
""" Basic Flask route """
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("templates/0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
