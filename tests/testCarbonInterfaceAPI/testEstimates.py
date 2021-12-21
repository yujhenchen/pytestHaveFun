import pytest_check as check
from estimatesClient import EstimatesClient


def test_post_flight_estimates(params):
    requestBody = {
        "type": "flight",
        "legs": [
            {"departure_airport": "nce", "destination_airport": "arn"}
        ]
    }
    response = EstimatesClient.post_flight_estimates(
        params['apiKey'], requestBody)
    print(response)


def test_get_all_estimates(params):
    response = EstimatesClient.get_all_estimates(params['apiKey'])
    print(response)
