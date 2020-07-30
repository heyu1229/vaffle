# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------店铺管理员 品牌管理员申请列表----------------------
class Brands(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------店铺管理员申请列表----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 38

        payload = {"normal_member_uuid":self.member_uuid,"type":"shop","page":1,"business_id":"54274"}
        result = self.requests.interface_requests_payload("9ccc4119-f04d-43b5-9c0f-c3cf679fe4c9", sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()