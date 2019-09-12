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

#---------------品牌主页----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------品牌主页----------------------------------
    def testcase_001(self):
        sheet_index = 11
        row = 2
        member_id='959'
        print ("testcase_001品牌主页:")
        payload ={"brand_id": 1,"normal_member_uuid":'1111fe8b-2ae9-4787-9371-0c5bb2dd8af1'}
        payload1 ={"brand_id": 1,"normal_member_id":'959'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row,payload1)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
