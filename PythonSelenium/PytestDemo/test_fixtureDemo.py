import pytest

@pytest.mark.usefixtures("setup")
class commonfixture:


    def test_firstDemo(self):
        print("I will execute first demo steps")

        def test_secondDemo(self):
            print("I will execute second demo steps")

            def test_thirdDemo(self):
                print("I will execute third demo steps")
