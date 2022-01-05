import pytest
import pytest_check as check


def test_user(params):
    print(params)
    # verify command line arguments
    check.equal(params['user'], "userA", "user should be userA")
    check.equal(params['password'], "00000", "password should be 00000")
