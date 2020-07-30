# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------获取收货地址（默认、所有）----------------------
class Address(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------获取收货地址（默认）----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 34
        print("testcase_001获取收货地址（默认）：")
        result = self.requests.interface_requests(self.member_uuid, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()