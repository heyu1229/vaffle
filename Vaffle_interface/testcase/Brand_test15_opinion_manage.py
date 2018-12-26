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

#---------------想法管理列表---------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------想法管理列表第一页数据----------------------------------

    def testcase_001(self):
        sheet_index = 11
        row = 20
        print ("testcase_001想法管理列表第一页数据:")

        member_id = '34791'
        payload = {"page": 1,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        print(result)
        list=result["data"]["list"]
        global last_id
        last_id = list[9]["post_id"]
        print("last_id=",last_id)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------想法管理列表第2页数据----------------------------------

    def testcase_002(self):
        sheet_index = 11
        row = 21
        print ("testcase_002想法管理列表第2页数据:")

        member_id = '34791'
        payload = {"page": 2,"last_id":last_id,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()
