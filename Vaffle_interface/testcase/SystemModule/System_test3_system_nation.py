# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url


#---------------所有国家列表----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()

    #-----------------所有国家列表----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 4
        print("testcase_001所有国家列表：")
        result=self.requests.interface_requests(self.member_uuid,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()