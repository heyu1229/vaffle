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

#---------------是否可以切换至指定身份----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()
       self.member_id = '745'

    #-----------------可以切换至指定身份----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 123

        print("testcase_001可以切换至指定身份：")
        payload = {"normal_member_id":745,"target_role":34791}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------不可以切换至指定身份----------------------------------
    def testcase_002(self):
        sheet_index = 0
        row = 124
        print("testcase_002不可以切换至指定身份：")
        payload = {"normal_member_id":745,"target_role":1111}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10107, result['code'])
        print("code返回值：10107")
if __name__ == "__main__":
    unittest.main()