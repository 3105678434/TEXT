import unittest

from common.read_add import build_add_data1
from tools import add
from parameterized import parameterized

# class Testadd(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(2,add(1,1))
#
#     def test2(self):
#         self.assertEqual(3, add(1, 2))
data = [(1, 1, 2), (1, 2, 3)]


class Testadd(unittest.TestCase):
    # @parameterized.expand(build_add_data())
    @parameterized.expand(build_add_data1())
    def testadd(self, a, b, expect):
        print(f'a:{a},b:{b},expect:{expect}')
        self.assertEqual(expect, add(a, b))


if __name__ == '__main__':
    print(build_add_data1())


