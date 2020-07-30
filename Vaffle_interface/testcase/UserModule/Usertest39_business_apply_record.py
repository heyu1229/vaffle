# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------申请店长、品牌管理记录----------------------
class Business_apply_record(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()


    #-----------------店铺管理员查看记录----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 39
        print("testcase_001店铺管理员查看记录：")
        payload = {"normal_member_uuid":self.member_uuid,"page":1}
        result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()