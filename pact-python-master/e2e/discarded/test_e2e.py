import atexit

import requests
import unittest

from pact import EachLike, SomethingLike, Term
from pact.consumer import Consumer
from pact.provider import Provider

pact = Consumer('consumer').has_pact_with(Provider('provider'), host_name='mockservice', port=1234)

pact.start_service()
atexit.register(pact.stop_service)


class BaseTestCase(unittest.TestCase):
    pass


class ExactMatches(BaseTestCase):
    def test_get_user_sparse(self):
        expected = {"status": "success",
                    "data": {"id": "24", "employee_name": "Doris Wilder", "employee_salary": "85600",
                             "employee_age": "23", "profile_image": ""}}
        (pact
         .given('a simple json blob exists')
         .upon_receiving('a request for a user')
         .with_request('get', '/users/Jonas')
         .will_respond_with(200, body=expected))

        with pact:
            result = requests.get('http://dummy.restapiexample.com/api/v1/employee/24')

        self.assertEqual(result.json(), expected)

    def test_get_user(self):
        # Provider Start
        expected = {"status": "success",
                    "data": {"id": "24", "employee_name": "Doris Wilder", "employee_salary": "85600",
                             "employee_age": "23", "profile_image": ""}}
        pact.given(
            'UserA exists and is not an administrator'
        ).upon_receiving(
            'a request for UserA'
        ).with_request(
            'GET', '/users/UserA'
        ).will_respond_with(200, body=expected)
        # PRovider End
        # Consumer Start
        with pact:
            result = requests.get('http://dummy.restapiexample.com/api/v1/employee/21')

        self.assertEqual(result, expected)
        # Consumer End.

