import atexit
import unittest

import requests
from pactman import Consumer, Provider, Term, Like
from pactman.verifier.pytest_plugin import pact_verifier

pact = Consumer('Consumer').has_pact_with(Provider('Provider'),
                                             use_mocking_server=False, pact_dir="C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master\\Pacts")

# pact.start_mocking()
# atexit.register(pact.stop_mocking)


class Generate_POC_PACTS(unittest.TestCase):

    def test_generate_pact_from_consumer_end(self):
        # Setting up Expected Response
        expected = {'skip': 0, 'limit': 150}

        pact.given(
            'A Support User exists and is not an administrator'
        ).upon_receiving(
            'a request for API support'
        ).with_request(
            method='GET',
            path='/api',
        ).will_respond_with(200, body=expected)

        # When a request is hit to Server, would it retrieve the expected data
        with pact:
            result = requests.get(pact.uri + '/api')

        self.assertEqual(result.json(), expected)



