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

#---------------用户加入、退出品牌---------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------用户加入品牌----------------------------------

    def testcase_001(self):
        sheet_index = 11
        row = 18
        print ("testcase_001用户加入品牌:")

        member_id = '980'
        payload = {"brand_id": 1 ,"status":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------用户退出品牌----------------------------------

    def testcase_002(self):
        sheet_index = 11
        row = 19
        print ("testcase_002用户退出品牌:")

        member_id = '980'
        payload = {"brand_id": 1, "status": 0}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
