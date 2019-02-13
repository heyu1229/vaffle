# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import time
import xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------话题提示功能----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------获取默认推荐话题----------------------------------
    def testcase_001(self):
        sheet_index = 9
        row = 1
        print("testcase_001获取默认推荐话题：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

            # -----------------获取根据关键字搜索得到的话题----------------------------------
    def testcase_002(self):
        sheet_index = 9
        row = 2
        print("testcase_002获取根据关键字搜索得到的话题：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------关键字为空---------------------------------
    def testcase_003(self):
        sheet_index = 9
        row = 3
        print("testcase_003关键字为空：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

if __name__=="__main__":
    unittest.main()
