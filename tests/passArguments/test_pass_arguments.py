import pytest


def test_user(params):
    print(params)
    # verify command line arguments
    assert params['user'] == "userA"
    assert params['password'] == "00000"
