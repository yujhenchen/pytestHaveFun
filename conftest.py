import pytest


def pytest_addoption(parser):
    parser.addoption("--var1", action="store",
                     default="value0", help="value0 or value1")
    parser.addoption("--var2", action="store",
                     default="value00", help="value00 or value11")


@pytest.fixture
def params(vars):
    params = {}
    params['var1'] = vars.config.getoption('--var1')
    params['var2'] = vars.config.getoption('--var2')
    if params['var1'] is None or params['var2'] is None:
        pytest.skip()
    return params
