import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass method execution.....')
    def setUp(self):
        print('setUp method execution.....')

    def testmethod1(self):
        print("test method1 cheecking login functionality in googlechrome")
        print('test method1 execution.....')
    def testmethod2(self):
        print("test method2 cheecking login functionality in firefox")
        print('test method2 execution.....')
        print(10/0)
    def testmethod3(self):
        print("test method3 cheecking login functionality in firefox")
        print('test method3 execution.....')
    def tearDown(self):
        print('tearDown method execution.....')
    def testmethod4(self):
        print("test method4 cheecking login functionality in firefox")
        print('test method4 execution.....')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass method execution.....')

unittest.main()