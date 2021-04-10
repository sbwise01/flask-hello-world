#!/usr/bin/env python

import os
from flask import Flask, request

app = Flask(__name__)
@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def main(u_path):
    if 'AWS_EXECUTION_ENV' in os.environ:
        exeenv = os.getenv('AWS_EXECUTION_ENV')
    else:
        exeenv = "NOT FOUND"
    if 'APP_NAME' in os.environ:
        appName = os.getenv('APP_NAME')
    else:
        appName = "N/A"

    return "Hello World ... welcome to Flask!  AWS_EXECUTION_ENV=%s, APP_NAME=%s, Path=%s" % (exeenv,appName,u_path)

if __name__ == "__main__":
    app.run()

