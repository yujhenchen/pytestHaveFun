import pytest
import random
# import pytest_check as check


@pytest.fixture
def data():
    nums = random.sample(range(0, 3), 3)
    print(nums)
    return nums


def test_first_num(data):
    # check.equal(data[0], 0)
    assert data[0] == 0


def test_second_num(data):
    # check.equal(data[1], 1)
    assert data[1] == 1


def test_third_num(data):
    # check.equal(data[2], 2)
    assert data[2] == 2
