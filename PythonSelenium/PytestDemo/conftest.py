import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataload():
    print("User profile data is loading....")
    return ["Kaya", "prasad", "Badave"]


@pytest.fixture(params=[("chrome","Prasad","Selenium"), ("firefox","Badave","python"), ("IE","Kavya","English")])
def crossBrowser(request):
    return request.param
