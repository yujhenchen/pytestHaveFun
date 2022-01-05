import pytest


def setup_module():
    print("setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


# def setup_class():
#     print("setup_class")


# def teardown_class():
#     print("teardown_class")


def setup_method():
    print("setup_method")


def teardown_method():
    print("teardown_method")


def setup():
    print("setup")


def teardown():
    print("teardown")


# test class
class TestClass(object):
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def test_A(self):
        print("test_A")
        assert "A" == "AA"

    def test_B(self):
        print("test_B")
        assert 1 == 1

    # load test data from conftest
    def test_user(self, params):
        print("test_user")
        defaultUser = "admin"
        assert defaultUser == params['user']

    # load test data from conftest
    def test_pwd(self, params):
        print("test_pwd")
        defaultUser = "123"
        assert defaultUser == params['password']
