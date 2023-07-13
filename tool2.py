import unittest

from tool import TestAdd

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))
unittest.TextTestRunner().run(suite)