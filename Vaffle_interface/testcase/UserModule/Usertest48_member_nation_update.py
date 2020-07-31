# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------更新用户所在国家----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------更新用户所在国家----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 48
        print("testcase_001 更新用户所在国家：")
        payload={"country_code":"CN"}
        result = self.requests.interface_requests_payload(self.member_uuid,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()