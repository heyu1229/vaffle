# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------新增店铺线索----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------店铺线索新增成功----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 8
        print ("testcase_001店铺线索新增成功:")

        obj = ({"week":[1,2],"start":"01:00","close":"03:00"},{"week":[4,5],"start":"05:00","close":"06:00"})
        business_hours = json.dumps(obj)
        payload = {"cover": "posts/153682373426094_960_ios.jpg", "address": "kangjian", "shop_name":"shop_lisa","business_hours":business_hours,"nation":"china","city":"shanghai","payment":"zhifubao","tel":"18833255555"}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()