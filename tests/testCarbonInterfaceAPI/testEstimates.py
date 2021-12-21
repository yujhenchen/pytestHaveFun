import pytest_check as check
from estimatesClient import EstimatesClient


def test_post_flight_estimates():
    return


def test_get_all_estimates():
    response = EstimatesClient.get_all_estimates()
    print(response)
    return
