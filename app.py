#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)
@app.route("/")
def main():
    return "Hello World ... welcome to Flask!"

if __name__ == "__main__":
    app.run()

