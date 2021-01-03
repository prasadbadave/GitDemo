import pytest


@pytest.mark.usefixtures("setup")

class fixtureAnnotation:
    def test_first(self):
        print("first file")

    def test_second(self):
        print("second file")

    def test_third(self):
        print("third file")