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

#---------------检测第三方是否注册----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------	检测第三方已注册----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 1
        print("testcase_001检测第三方已注册：")
        member_id='none'
        result=self.r.interface_requests(member_id,sheet_index,row)
        data=result['data']
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        self.assertEqual(1, len(data["list"]))
        print("推荐的用户昵称等于1，表示已经注册")


    #-----------------	检测第三方未注册----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_002(self):
        sheet_index = 6
        row = 2
        print("testcase_001检测第三方未注册：")
        member_id = 'none'
        result = self.r.interface_requests(member_id, sheet_index, row)
        data=result["data"]

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.assertEqual(5, len(data["list"]))
        print("推荐的用户昵称不等于1，表示未注册")



if __name__=="__main__":
    unittest.main()
