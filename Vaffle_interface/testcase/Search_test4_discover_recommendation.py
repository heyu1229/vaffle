# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------discover页推荐数据（用户、店铺）----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    # -----------------discover页推荐数据（用户、店铺）----------------------------------
    def testcase_001(self):
        sheet_index = 9
        row = 7
        print("testcase_001 discover页推荐数据（用户、店铺）：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------搜索reveal数据----------------------------------
    def testcase_002(self):
        sheet_index = 9
        row = 8
        print("testcase_002搜索reveal数据：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------搜索people数据---------------------------------
    def testcase_003(self):
        sheet_index = 9
        row = 9
        print("testcase_003搜索people数据：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------keywords为空---------------------------------
    def testcase_006(self):
        sheet_index = 9
        row = 10
        print("testcase_006keywords为空：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

if __name__=="__main__":
    unittest.main()
