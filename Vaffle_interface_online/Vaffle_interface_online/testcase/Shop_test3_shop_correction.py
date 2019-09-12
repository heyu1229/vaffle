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

#---------------提交店铺纠错信息----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.requests = FuncRequests()
       self.member_id = 'none'

    #-----------------店铺纠错信息提交成功----------------------------------
    def testcase_001(self):
        sheet_index = 11
        row = 5

        member_id = "960"
        print ("testcase_001提交店铺纠错信息:")
        obj = ({"week":[1,2],"start":"01:00","close":"03:00"},{"week":[4,5],"start":"05:00","close":"06:00"})
        business_hours = json.dumps(obj)
        payload = {"shop_id":"29388","tel":"18888066666","address":"address111","shop_name":"shop_name111","business_hours":business_hours,"other":" 111"}
        result = self.requests.interface_requests_payload(member_id,sheet_index,row,payload)
        try:
            self.assertEqual(10000, result['code'])
        except:
            self.assertEqual(10087, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()