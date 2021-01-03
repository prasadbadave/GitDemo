# Pytest file name should always start with test_
# pytest method should start or end with test_ or _test
import pytest


@pytest.mark.sanity
def test_mytestMethod():
    print("This is my first pytest")

@pytest.mark.xfail
def test_myMethod():
    print("This is my second pytest")
