import atexit
import unittest

import requests
from pactman import Consumer, Provider, Term, Like
from pactman.verifier.pytest_plugin import pact_verifier

pact = Consumer('ConsumerPOC').has_pact_with(Provider('Provider'),
                                             use_mocking_server=True, pact_dir="C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master")

pact.start_mocking()
atexit.register(pact.stop_mocking)


class GetUserInfoContract(unittest.TestCase):

    def test_generate_pact_from_consumer_end(self):
        # Setting up Expected Response
        expected = {'skip': 0, 'limit': 150}
        # Simulating an Real HTTP Server
        pact.given(
            'User ML exists and is not an administrator'
        ).upon_receiving(
            'a request for ML'
        ).with_request(
            method='GET',
            path='/api',
        ).will_respond_with(200, body=expected)

        # When a request is hit to Server, would it retrieve the expected data
        with pact:
            result = requests.get(pact.uri + '/api')

        self.assertEqual(result.json(), expected)

    ''' def test_get_MS(self):
        # Provider Start
        expected = {
            'from': '2020-01-21T12:30:00+11:00',
            'to': '2020-01-21T12:35:03.953+11:00',
            'skip': 0,
            'limit': Like(2),
            'total': 0,
            'presenceChanges': []
        }
        pact.given(
            'User ML exists and is not an administrator'
        ).upon_receiving(
            'a request for ML'
        ).with_request(
            method='GET',
            path='/api/s-marshall/v1/store/feeds/presenceChanges?from=2020-01-21T12%3A30%3A00.0%2B11%3A00&amp; to=2020-01-21T12%3A35%3A03.953%2B11%3A00&amp; skip=0&amp; limit=150 HTTP/1.1',
            body={},
            headers={'Content-Type': 'application/json', 'X-Client-ID': '7f2d217a69704b5d8971fe501a0582ad', "X-Client-Secret": "765eC5Ea511D4a169f3e60B1b0809E70", "Marshall-End-User": "AJ", "Marshall-System-User": "SFDC"},
        ).will_respond_with(200, body=expected)
        # PRovider End
        # Consumer Start
        with pact:
            result = requests.get('http://s-marshall-stage.au-s1.cloudhub.io/api/s-marshall/v1/store/feeds/presenceChanges?from=2020-01-21T12%3A30%3A00.0%2B11%3A00&to=2020-01-21T12%3A35%3A03.953%2B11%3A00&skip=0&limit=150')

        self.assertEqual(result.json(), {
            'from': '2020-01-21T12:30:00+11:00',
            'to': '2020-01-21T12:35:03.953+11:00',
            'skip': 0,
            'limit': 150,
            'total': 0,
            'presenceChanges': []
        })
        # Consumer End.



'''

    ''' def test_get_MS_real(self):
        # Provider Start
        expected = {
            'from': '2020-01-21T12:30:00+11:00',
            'to': '2020-01-21T12:35:03.953+11:00',
            'skip': 0,
            'limit': Like(150),
            'total': 0,
            'presenceChanges': []
        }
        pact.given(
            'User ML exists and is not an administrator'
        ).upon_receiving(
            'a request for ML'
        ).with_request(
            method='GET',
            path='api/x-salesforce/v1/accounts/001O000001PxCIL/ssolink',
            body={},
            headers={'Content-Type': 'application/json', 'X-Client-ID': '7f2d217a69704b5d8971fe501a0582ad', "X-Client-Secret": "765eC5Ea511D4a169f3e60B1b0809E70", "Marshall-End-User": "AJ", "Marshall-System-User": "SFDC"},
        ).will_respond_with(200, body=expected)
        # PRovider End
        # Consumer Start
        with pact:
            result = requests.get('https://x-salesforce-test.au-s1.cloudhub.io/api/x-salesforce/v1/accounts/001O000001PxCIL/ssolink')

        self.assertEqual(result.json(), expected)
        # Consumer End.
'''


