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

#---------------互相关注列表----------------------
class Follow_Followers(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------查看我的朋友----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 9
        print("testcase_001查看我的朋友：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        data = result["data"]
        try:
            self.assertEqual([], data["list"])
            print("朋友列表为空")
        except AssertionError as e:
            print("朋友列表不为空")

if __name__=="__main__":
    unittest.main()