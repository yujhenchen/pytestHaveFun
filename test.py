import pytest_check as check


def test_fruits(*fruits):
    apple = "apple"
    orange = "orange"

    print(fruits)
    print(fruits[0])
    print(fruits[1])

    check.equal(fruits[0], apple, "First fruit should be " + apple)
    check.equal(fruits[1], orange, "Second fruit should be " + orange)
    check.equal(fruits[2], apple, "Third fruit should be " + apple)


test_fruits("apple", "banana", "orange")
