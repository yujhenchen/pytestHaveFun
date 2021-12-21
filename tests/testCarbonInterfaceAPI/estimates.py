import requests


class EstimatesClient(object):
    url = "https://www.carboninterface.com/api/v1/"
    path = "estimates"

    def __init__(self):
        super().__init__()

    def get_request_headers(apiKey):
        return {'Authorization': "Bearer " + apiKey, 'Content-Type': 'application/json'}

    def post_flight_estimates(apiKey, requestBody):
        response = requests.post(url=EstimatesClient.url + EstimatesClient.path,
                                 headers=EstimatesClient.get_request_headers(
                                     apiKey),
                                 json=requestBody)
        responseJson = response.json()
        return response.status_code, responseJson

    def get_all_estimates(apiKey, *querieargs):
        response = requests.get(
            url=EstimatesClient.url + EstimatesClient.path, headers=EstimatesClient.get_request_headers(apiKey))

        # print("status code: " + str(response.status_code))
        # print("response headers: "+str(response.headers))
        responseJson = response.json()
        # print(responseJson)
        return response.status_code, responseJson
