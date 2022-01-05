dataMap = {}


def setup_module():
    print("setup_module")
    dataMap["A"] = 1
    dataMap["B"] = 2
    dataMap["C"] = 3


def teardown_module():
    print("teardown_module")


def test_check_first():
    print("test_check_first")
    assert dataMap["A"] == 1


def test_check_second():
    print("test_check_second")
    assert dataMap["B"] == 0


def test_check_third():
    print("test_check_third")
    assert dataMap["C"] == 3
