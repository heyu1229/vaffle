# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd

from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------用户个人中心【简化】---------------------
class Passport_retrievepassword(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()


    def testcase_001(self):
        sheet_index = 0
        row = 56
        print("testcase_001 用户个人中心【简化】：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()