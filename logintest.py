import unittest

from logins import login


class TestLogin(unittest.TestCase):
    def test_a(self):
        if "ok" == login('admin', '123456'):
            print('通过')
        else:
            print('不通过')

    def test_b(self):
        if "no" == login('root', '123456'):
            print('通过')
        else:
            print('不通过')
