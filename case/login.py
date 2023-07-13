import unittest

from common.read_add import build_login_data
from parameterized import parameterized

from logins import login


class TestLogin(unittest.TestCase):
    @parameterized.expand(build_login_data)
    def test_login(self, username, password, expect):
        print(f'username:{username},password:{password},expect:{expect}')
        self.assertEqual(expect, login(username, password))
