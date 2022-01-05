import pytest


class TestClass(object):
    dataMap = {}

    def setup_class(self):
        self.dataMap["A"] = 1
        self.dataMap["B"] = 2
        self.dataMap["C"] = 3

    def teardown_class(self):
        self.dataMap.clear()

    def test_check_first(self):
        print("test_check_first")
        assert self.dataMap["A"] == 1

    def test_check_second(self):
        print("test_check_second")
        assert self.dataMap["B"] == 0

    def test_check_third(self):
        print("test_check_third")
        assert self.dataMap["C"] == 3
