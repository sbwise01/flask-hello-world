#!/usr/bin/env python

import os
from flask import Flask

app = Flask(__name__)
@app.route("/")
def main():
    if 'AWS_EXECUTION_ENV' in os.environ:
        exeenv = os.getenv('AWS_EXECUTION_ENV')
    else:
        exeenv = "NOT FOUND"
    return "Hello World ... welcome to Flask!  AWS_EXECUTION_ENV=%s" % exeenv

if __name__ == "__main__":
    app.run()

