import pytest


class TestClass(object):
    dataMap = {}

    @pytest.fixture(autouse=True)
    def _request_params(self, params):
        print("_request_params")
        self.params = params

    def setup_class(self):
        print("setup_class")
        self.dataMap["user"] = "admin"
        self.dataMap["password"] = "123"

        # print(self.params['user'])
        # print(self.params['password'])

    def teardown_class(self):
        print("teardown_class")
        self.dataMap.clear()

    def test_user(self):
        print("test_user")
        assert self.dataMap["user"] == self.params['user']

    def test_pwd(self):
        print("test_pwd")
        assert self.dataMap["password"] == self.params['password']
