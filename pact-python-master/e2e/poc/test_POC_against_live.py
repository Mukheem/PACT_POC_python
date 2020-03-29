import atexit
import unittest

import requests
from pactman import Consumer, Provider, Term, Like
from pactman.verifier.pytest_plugin import pact_verifier

pact = Consumer('SF').has_pact_with(Provider('MULESOFT'),
                                             use_mocking_server=False, pact_dir="C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master\\Pacts")

# pact.start_mocking()
# atexit.register(pact.stop_mocking)


class Generate_POC_PACTS(unittest.TestCase):

    def test_generate_pact_for_original_API(self):
        # Setting up Expected Response
        expected = {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"},"ad":{"company":"StatusCode Weekly","url":"http://statuscode.org/","text":"A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things."}}

        pact.given(
            'A Support User exists and is not an administrator'
        ).upon_receiving(
            'a request for API support'
        ).with_request(
            method='GET',
            path='/api/users/2',
        ).will_respond_with(200, body=expected)

        # When a request is hit to Server, would it retrieve the expected data
        with pact:
            result = requests.get(pact.uri + '/api/users/2')

        self.assertEqual(result.json(), expected)

