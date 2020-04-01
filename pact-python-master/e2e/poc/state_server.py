import json

from http_server_mock import HttpServerMock
from flask import Flask, request
import requests

app = HttpServerMock(__name__)


@app.route('/setup', methods=['POST'])
def hello():
    print(request.json)
    # Setting up state as needed by the PACT. i.e., Consumer to proceed with provider testing.
    if request.json['state'] == 'A Support User exists and is not an administrator':
        return {'State': True}
    elif request.json['state'] == 'A Support user has access to hit post request':
        return {'State': True}
    else:
        return {'State': False}


with app.run("localhost", 8082):
    r = requests.get("http://localhost:8082/")
    print(r.status_code == 200)
    print(r.text == "Hello world")
