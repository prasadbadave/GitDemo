import pytest



@pytest.mark.usefixtures("dataload")
class Testdataload:

    def test_dataload(self,dataload):
        print("data is loading from conftest file")
        print(dataload)

