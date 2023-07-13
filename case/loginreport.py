import unittest

from app import BASE_DIR
from case.login import TestLogin
from htmltestreport import HTMLTestReport

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
runner = HTMLTestReport(BASE_DIR + '/report/login_report.html')
runner.run(suite)