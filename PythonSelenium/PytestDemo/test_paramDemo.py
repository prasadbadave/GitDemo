import pytest


@pytest.mark.usefixtures("crossBrowser")
class TestParam:
    def test_crossbrowsertest(crossBrowser):
        print(crossBrowser[1])
