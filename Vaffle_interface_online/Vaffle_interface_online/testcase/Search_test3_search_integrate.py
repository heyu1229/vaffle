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

#---------------综合搜索功能----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    # -----------------搜索post数据----------------------------------
    def testcase_001(self):
        sheet_index = 8
        row = 5
        print("testcase_001搜索post数据：")
        member_id = "960"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------搜索reveal数据----------------------------------
    def testcase_002(self):
        sheet_index = 8
        row = 6
        print("testcase_002搜索reveal数据：")
        member_id = "960"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------搜索people数据---------------------------------
    def testcase_003(self):
        sheet_index = 8
        row = 7
        print("testcase_003搜索people数据：")
        member_id = "960"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
