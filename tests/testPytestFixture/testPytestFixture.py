import pytest
import random
import pytest_check as check

'''
Use different scope of the fixture to control the invoking of the fixture function: function, class, module, package, session
'''


@pytest.fixture(scope='module')
def module_data():
    nums = random.sample(range(0, 3), 3)
    print("module_data: " + str(nums))
    return nums


@pytest.fixture(scope='session')
def session_data():
    nums = random.sample(range(4, 7), 3)
    print("session_data: " + str(nums))
    return nums


@pytest.fixture(scope='function')
def function_data():
    nums = random.sample(range(8, 11), 3)
    print("function_data: " + str(nums))
    return nums


def test_first_num(module_data, session_data, function_data):
    # assert module_data[0] == 0
    check.equal(module_data[0], 0)
    check.equal(session_data[0], 4)
    check.equal(function_data[0], 8)


def test_second_num(module_data, session_data, function_data):
    # assert module_data[1] == 1
    check.equal(module_data[1], 1)
    check.equal(session_data[0], 5)
    check.equal(function_data[0], 9)


def test_third_num(module_data, session_data, function_data):
    # assert module_data[2] == 2
    check.equal(module_data[2], 2)
    check.equal(session_data[0], 6)
    check.equal(function_data[0], 10)
