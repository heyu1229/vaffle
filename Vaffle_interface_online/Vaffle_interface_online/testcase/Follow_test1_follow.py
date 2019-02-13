#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc
import json
import xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------关注----------------------
class Follow(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------关注、取消关注----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 1
        print("testcase_001关注、取消关注:")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------用户不存在----------------------------------
    def testcase_002(self):
        sheet_index = 2
        row = 2
        print("testcase_002用户不存在:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10040, result["code"])
        print("code返回值：10040")

if __name__=="__main__":
    unittest.main()