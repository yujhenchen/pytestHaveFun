import pytest_check as check
from estimatesClient import EstimatesClient


def test_post_flight_estimates(params):
    return


def test_get_all_estimates(params):
    response = EstimatesClient.get_all_estimates(params['apiKey'])
    print(response)
    return
