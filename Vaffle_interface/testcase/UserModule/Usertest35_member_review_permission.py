# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url


#---------------判断用户是否可以发布评测post----------------------
class Review_permission(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------判断用户是否可以发布评测post----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 35
        print("testcase_001判断用户是否可以发布评测post：")
        result = self.requests.interface_requests(self.member_uuid, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()