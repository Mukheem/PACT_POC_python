import atexit
import os
import unittest

import pytest
import requests
from pactman import Consumer, Provider

from pactman.verifier.broker_pact import BrokerPacts, pact_id
from pactman.verifier.result import PytestResult

pytestConfig = {
      "provider" : 'Provider',
      "providerBaseUrl " : 'http://localhost:8082',
      "providerStatesSetupUrl" : 'http://localhost:8082/setup',
      "pactBrokerUrl" : 'C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master\\Pact',
      "publishVerificationResult" : True
}


@pytest.mark.parametrize('pact_verifier', [[pytestConfig, requests.get("http://localhost:8081/api") ]], indirect=True)
def test_pacts(self, pact_verifier):
    pact_verifier.verify("http://localhost:8081", "http://localhost:8082/setup")



# @pytest.mark.parametrize('pact', BrokerPacts('Provider',
#                                            pact_broker='C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master',
#                                            result_factory=PytestResult), ids=pact_id)

# def test_pacts():
# pact_verifier.verify("http://localhost:8155/", "User ML exists and is not an administrator")
from pactman.mock import pact

from pactman.verifier.broker_pact import BrokerPacts, pact_id, BrokerPact
from pactman.verifier.result import PytestResult
from pactman.verifier.pytest_plugin import pact_verifier, PytestPactVerifier
# a = PytestPactVerifier("C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master", '1.0',
# "C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master\\ConsumerPOC-Provider-pact.json", "ConsumerPOC")

# def test_pact_against_provider():
# a.verify('localhost:8081/',"User ML exists and is not an administrator")


# Start provider

# try:
#     pact_files = (
#         f for f in os.listdir("C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master\\Pact")
#        if os.path.isfile(f) and os.path.splitext(f)[1] == '.json'
#    )
#   for pact_file in pact_files:
#        pact = BrokerPact.load_file(pact_file, PytestResult)
#      for interaction in pact.interactions:
#           interaction.verify("http://localhost:8081", "C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master\\ConsumerPOC-Provider-pact.json")
#           assert interaction.result.success
# finally:
#    pass
# Stop provider

# @pytest.mark.parametrize('pact', BrokerPacts('Provider',
#                                             pact_broker='C:\\Users\\abdulsha\\PycharmProjects\\pact-python-master',
#                                             result_factory=PytestResult), ids=pact_id)
# def test_pacts(live_server, pact, SETUP_STATE_URL=None):
#    pact.verify(live_server.url, live_server.url + SETUP_STATE_URL)


# from django.contrib.auth.models import User
# from pactman.verifier.verify import ProviderStateMissing


# def provider_state(name, **params):
#    if name == 'User ML exists and is not an administrator':
#        User.objects.create(username='pat', fullname=params['fullname'])
#    else:
#        raise ProviderStateMissing(name)


# def test_pacts(live_server, pact_verifier):
#    pact_verifier.verify(live_server.url, provider_state)
