import requests


class EstimatesClient(object):
    url = "https://www.carboninterface.com/api/v1/"
    path = "estimates"

    def __init__(self):
        super().__init__()

    def post_flight_estimates(apiToken, params):

        return

    def get_all_estimates(apiKey, *querieargs):
        getRequest = requests.get(
            url=EstimatesClient.url + EstimatesClient.path, headers={'Authorization': apiKey})
        response = getRequest.json()
        print(response)
        return
