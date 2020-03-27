import json

from http_server_mock import HttpServerMock
from flask import Flask, request
import requests
app = HttpServerMock(__name__)


@app.route('/setup', methods=['POST'])
def hello():
    print('Yaay...I am called')
    print(request.json)
    if request.json['state'] == 'User ML exists and is not an administrator':
        print('Yaay')
        return {'skip': 0, 'limit': 151}
    else:
        print('daai')
        #return {'skip': 0, 'limit': 150}



with app.run("localhost", 8082):
    r = requests.get("http://localhost:8082/")
    print(r.status_code == 200)
    print(r.text == "Hello world")