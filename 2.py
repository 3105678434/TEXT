import unittest
suite = unittest.TestLoader().discover('.','test*.py')
# unittest.TextTestRunner().run(suite)
runner = unittest.TextTestRunner()
runner.run(suite)
