import unittest


class TestAssert(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(10, 10)

    def test_assert(self):
        self.assertEqual(10, 11)

    def test_in(self):
        self.assertIn('admin', '欢迎admin')
