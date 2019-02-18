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

#---------------@用户提示功能----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------获取默认推荐@用户----------------------------------
    def testcase_001(self):
        sheet_index = 8
        row = 3
        print("testcase_001获取默认推荐@用户：")
        member_id = "960"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------获取根据关键字搜索得到的用户----------------------------------
    def testcase_002(self):
        sheet_index = 8
        row = 4
        print("testcase_002获取根据关键字搜索得到的用户：")
        member_id = "960"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
