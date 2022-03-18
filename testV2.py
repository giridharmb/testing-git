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


@app.route('/testV2', methods=['GET'])
def test():
    data = {"x": 123, "y": 456}
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response


if __name__ == "__main__":
    syslog.syslog("starting api...")
    app.run(debug=True, port=9000, host='127.0.0.1')
