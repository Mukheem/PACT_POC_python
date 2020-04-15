import atexit
import unittest

import requests
from pactman import Consumer, Provider, Term, Like
from pactman.verifier.pytest_plugin import pact_verifier

# Establishing a connection between Provider and Consumer and assigning it to Pact variable
pact = Consumer('SF').has_pact_with(Provider('MULESOFT'), file_write_mode="merge",
                                             use_mocking_server=False, pact_dir="C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master\\Pacts")

# pact.start_mocking()
# atexit.register(pact.stop_mocking)


class Generate_POC_PACTS(unittest.TestCase):

    def test_generate_pact_for_original_API(self):
        # Setting up Expected Response
        expected = {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"},"ad":{"company":"StatusCode Weekly","url":"http://statuscode.org/","text":"A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things."}}

        # Mocking Provider i.e.,
        # What should be the response when specific type of request is hit with given pre-requisite
        pact.given(
            'A Support User exists and is not an administrator'
        ).upon_receiving(
            'a request for API support'
        ).with_request(
            method='GET',
            path='/api/users/2',
        ).will_respond_with(200, body=expected)

        # When a request is hit to Mock Server, is it retrieving the expected data ?
        with pact:
            result = requests.get(pact.uri + '/api/users/2')

        self.assertEqual(result.json(), expected)

    def test_generate_pact_post_register(self):
        # Setting up Expected Response
        expected = {"id": Like(4), "token": Like("QpwL5tke4Pnpja7X5")}

        input_data = {"email": "eve.holt@reqres.in", "password": "gun"}
        pact.given(
            'A Support user has access to hit post request'
        ).upon_receiving(
            'a request POST'
        ).with_request(
            method='POST',
            path='/api/register',
            body=input_data,
            # headers={'Content-Type': 'application/json'},
        ).will_respond_with(200, body=expected) # This will respond with actual sample data in it. But not with the objects

        # When a request is hit to Server, would it retrieve the expected data
        with pact:
            result = requests.post(pact.uri + '/api/register', json=input_data)

        self.assertEqual(result.json(), {"id": 4, "token": "QpwL5tke4Pnpja7X5"})
