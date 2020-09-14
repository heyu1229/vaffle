'''
@create : lisa
@file :helloworld.py
@Date :2020/9/14
@desc :

'''
import unittest



class SignIn(unittest.TestCase):

    def setUp(self):
        self.member_uuid = 'none'


    def testcase_001(self):
        print("hello world")
if __name__ == '__main__':
    unittest.main()