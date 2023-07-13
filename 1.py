import unittest

from test import TestDemo
from test2 import TestDemo2

suite = unittest.TestSuite()
suite.addTest(TestDemo('test_method1'))
suite.addTest(TestDemo('test_method2'))
suite.addTest(TestDemo2('test_method1'))
suite.addTest(TestDemo2('test_method2'))
runner = unittest.TextTestRunner()
runner.run(suite)
