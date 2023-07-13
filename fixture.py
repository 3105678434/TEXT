import unittest
class TestLongin(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        print(1.)

    @classmethod
    def tearDownClass(cls) -> None:
        print(5.)

    def setUp(self) -> None:
        print(1)

    def tearDown(self) -> None:
        print(5)

    def test_1(self):
        print('2')

    def test_2(self):
        print('3')

    def test_3(self):
        print('4')