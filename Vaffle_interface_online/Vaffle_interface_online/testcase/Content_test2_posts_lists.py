#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc,xlrd
import json,time
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests
#---------------discover video列表----------------------
class List(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()


    #-----------------首页动态列表post 第1页----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 2
        print("testcase_001首页动态列表post 第1页:")
        member_id="960"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

   #-----------------首页动态列表location 第1页----------------------------------
    def testcase_002(self):

        sheet_index = 1
        row = 3
        print("testcase_002首页动态列表location 第1页-:")
        member_id="960"
        result = self.r.interface_requests(member_id, sheet_index, row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

   #-----------------首页动态列表me 第1页----------------------------------
    def testcase_003(self):

        sheet_index = 1
        row = 4
        print("testcase_003首页动态列表me 第1页:")
        member_id="960"
        result = self.r.interface_requests(member_id, sheet_index, row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()