import unittest

from logintest import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
unittest.TextTestRunner().run(suite)
