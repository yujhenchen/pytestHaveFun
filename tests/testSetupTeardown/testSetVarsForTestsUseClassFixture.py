import pytest


class TestClass(object):
    dataMap = {}

    def setup_class(self, params):
        self.dataMap["user"] = params['user']
        self.dataMap["password"] = params['password']

    def teardown_class(self, params):
        self.dataMap.clear()

    def test_user(self, params):
        print("test_user")
        assert self.dataMap["user"] == "admin"

    def test_pwd(self, params):
        print("test_pwd")
        assert self.dataMap["password"] == "123"
