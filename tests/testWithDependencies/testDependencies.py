import pytest
import pytest_check as check


def test_first():
    check.is_true(True, "test_first should be true")


@pytest.mark.depends(on=['test_second'])
def test_third():
    check.is_true(True, "test_third should be true")


@pytest.mark.depends(on=['test_first'])
def test_second():
    check.is_true(False, "test_second should be true")
