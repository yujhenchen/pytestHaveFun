import pytest
import pytest_check as check


@pytest.mark.run(order=1)
def test_first():
    check.is_true(False, "test_first should be true")


@pytest.mark.run(order=3)
def test_third():
    check.is_true(True, "test_third should be true")


@pytest.mark.run(order=2)
def test_second():
    check.is_true(True, "test_second should be true")
