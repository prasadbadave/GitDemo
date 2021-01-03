import pytest

@pytest.mark.skip
def test_failedTestDemo():
    msg = "Hello"
    assert msg == "Hi, this test case is failed"

@pytest.mark.sanity
def test_addition():
    a = 2
    b = 6
    assert a + 2 == 6, "Addition"


def test_mytest():
    a = 7
    b = 14
    assert a + 7 == 14, "Addition"
