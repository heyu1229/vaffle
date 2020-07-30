# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------获取管理店铺 管理品牌的菜单项----------------------
class Brands(unittest.TestCase):

    def setUp(self):
        self.member_uuid = "9ccc4119-f04d-43b5-9c0f-c3cf679fe4c9"
        self.requests = FuncRequests ()

    #-----------------获取管理店铺的菜单项----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 37
        print("testcase_001获取管理店铺的菜单项：")
        payload = {"normal_member_uuid":self.member_uuid,"type":"shop"}
        #result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row,payload)
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()