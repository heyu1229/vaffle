# -*- coding:UTF-8 -*-
import unittest
import requests,gc
import sys,time

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------第三方登录接口----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------第三方facebook登录成功----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 3
        print("testcase_001第三方facebook登录成功：")
        member_id = "none"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------第三方twitter登录成功----------------------------------
    # -----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------

    def testcase_002(self):
        sheet_index = 6
        row = 4
        print("testcase_002第三方twitter登录成功：")
        member_id = "none"
        result = self.r.interface_requests(member_id, sheet_index, row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------第三方vk登录成功----------------------------------
    # -----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_003(self):
        sheet_index = 6
        row = 5
        print("testcase_003第三方vk登录成功：")
        member_id = "none"
        result = self.r.interface_requests(member_id, sheet_index, row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # -----------------不支持的第三方--------------------------
    def testcase_004(self):
        sheet_index = 6
        row = 6
        print("testcase_004不支持的第三方：")
        member_id = "none"
        result = self.r.interface_requests(member_id, sheet_index, row)

        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

    # -----------------第三方INS登录成功----------------------------------
    def testcase_005(self):
        sheet_index = 6
        row = 10
        print ( "testcase_003第三方ins登录成功：" )
        member_id = "none"
        result = self.r.interface_requests(member_id, sheet_index, row)

        self.assertEqual ( 10000, result["code"] )
        print ( "code返回值：10000" )

if __name__=="__main__":
    unittest.main()
