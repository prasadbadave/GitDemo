import pytest


@pytest.mark.usefixtures("setup")
class TestDemo:

    def test_firstclass(self):
        print("first class")

    def test_secondclass(self):
        print("second class")

    def test_thirdclass(self):
        print("thirdclass")