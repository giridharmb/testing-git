import ssl
import json
import requests
from flask import Flask, request
from flask import jsonify
from flask import Response
from flask import make_response
import logging
import logging.handlers
import pprint
import syslog

syslog.syslog("this is a test message")

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/api/v1/getData", methods=['GET'])
def get_data():
    if request.method == "GET":
        syslog.syslog("request : GET : /api/v1/getData")
        response = make_response()
        data = {"a": 123, "b": "hello world", "c": [1, 2, 3, 4, 5, 6], "d": {"a1": 11, "a2": 22}}
        response = jsonify(data)
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Methods', '*')
        return response


if __name__ == "__main__":
    syslog.syslog("starting api...")
    app.run(debug=True, port=8000, host='127.0.0.1')
