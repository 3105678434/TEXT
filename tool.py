import unittest
from tools import add


class TestAdd(unittest.TestCase):
    def test_1(self):
        if 2 == add(1, 1):
            print(f'用例{1},{1},{2}通过')
        else:
            print(f'用例{1},{1},{2}不通过')
