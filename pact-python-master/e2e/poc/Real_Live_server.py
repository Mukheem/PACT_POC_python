from http_server_mock import HttpServerMock
from flask import Flask
import requests

app = HttpServerMock(__name__)


@app.route('/api')
def hello():
    return {'skip': 0, 'limit': 150}


@app.route('/api/details')
def hell():
    return {'skip': 0}

@app.route('/user', methods=['POST'])
def user():
    return {'user' : 'Muqeem'}

with app.run("localhost", 8081):
    r = requests.get("http://localhost:8081/")
    print(r.status_code == 200)
    print(r.text == "Hello world")
