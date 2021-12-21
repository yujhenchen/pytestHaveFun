import requests


class EstimatesClient(object):
    url = "https://www.carboninterface.com/api/v1/"
    path = "estimates"

    def __init__(self):
        super().__init__()

    def post_flight_estimates(params):

        return

    def get_all_estimates(*querieargs):
        getRequest = requests.get(
            url=EstimatesClient.url + EstimatesClient.path)
        response = getRequest.json()
        print(response)
        return
