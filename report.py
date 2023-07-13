import unittest
from htmltestreport import HTMLTestReport

from add import Testadd
from add import Testadd

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Testadd))

runner = HTMLTestReport('report/test_add_report.html', '加法', 'xxx')
runner.run(suite)
