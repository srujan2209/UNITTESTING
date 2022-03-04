import unittest

class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method execution.....')

    def testmethod1(self):
        print("test method1 cheecking login functionality in googlechrome")
        print('test method1 execution.....')
    def testmethod2(self):
        print("test method2 cheecking login functionality in firefox")
        print('test method2 execution.....')
    def tearDown(self):
        print('tearDown method execution.....')
unittest.main()

