import pytest


def pytest_addoption(parser):
    parser.addoption("--user", action="store",
                     default="userA", help="userA or userB")
    parser.addoption("--password", action="store",
                     default="00000", help="Please provide corresponding passwords")

    # for api testing use
    parser.addoption("--apiKey", action="store",
                     default="00000", help="Please provide API key")


@pytest.fixture
def params(request):
    params = {}
    params['user'] = request.config.getoption('--user')
    params['password'] = request.config.getoption('--password')

    # for api testing use
    params['apiKey'] = request.config.getoption('--apiKey')
    # if params['user'] is None or params['password'] is None:
    #     pytest.skip()
    return params
