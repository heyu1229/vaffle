744# -*- coding:UTF-8 -*-
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

#---------------新版本检测----------------------
class System_version(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()
        self.version = Version().test_version()

    #-----------------新版本检测----------------------------------
    def testcase_001(self):
        # url2 =self.url+"/interservice/version"
        # r = requests.post (url2)
        sheet_index = 3
        row = 1
        print("testcase_001新版本检测：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        if self.version =="2.6.0":
            self.assertEqual(10033, result["code"])
            print("code返回值：10033，No new version")
        else :
            self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()