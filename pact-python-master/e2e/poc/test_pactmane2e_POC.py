import atexit
import unittest

import requests
from pactman import Consumer, Provider, Term, Like
from pactman.verifier.pytest_plugin import pact_verifier

pact = Consumer('Consumer').has_pact_with(Provider('Provider'),
                                          file_write_mode="override",
                                          use_mocking_server=False,
                                          pact_dir="C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master\\Pacts")


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

    """def test_generate_pact_post_request(self):
        # Setting up Expected Response
        expected = {"name": "Mukheem", "job": "Automation QA", "id": Like("1"),
                    "createdAt": Term('\d+-\d+-\d+T\d+:\d+:\d+z+', '2020-03-31T15:29:49.173Z')}

        input_data = {"name": "Mukheem", "job": "Automation QA"}
        pact.given(
            'A Support user has access to hit post request'
        ).upon_receiving(
            'a request POST'
        ).with_request(
            method='POST',
            path='/api/users',
            body=input_data,
            # headers={'Content-Type': 'application/json'},
        ).will_respond_with(201, body=expected)

        # When a request is hit to Server, would it retrieve the expected data
        with pact:
            result = requests.post(pact.uri + '/api/users', json=input_data)

        self.assertEqual(result.json(), {"name": "Mukheem", "job": "Automation QA", "id": "1",
                                         "createdAt": '2020-03-31T15:29:49.173Z'})
                                         

    def test_generate_pact_post_register(self):
        # Setting up Expected Response
        expected = {"id": Like(4), "token": Like("QpwL5tke4Pnpja7X5")}

        input_data = {"email": "eve.holt@gmail.com", "password": "gun"}
        pact.given(
            'A Support user has access to hit post request'
        ).upon_receiving(
            'a request POST'
        ).with_request(
            method='POST',
            path='/api/register',
            body=input_data,
            # headers={'Content-Type': 'application/json'},
        ).will_respond_with(200, body=expected)

        # When a request is hit to Server, would it retrieve the expected data
        with pact:
            result = requests.post(pact.uri + '/api/register', json=input_data)

        self.assertEqual(result.json(), {"id": 4, "token": "QpwL5tke4Pnpja7X5"})
"""