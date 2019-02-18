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

#---------------第三方分享回调接口----------------------
class Post_share(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------第三方分享回调----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 8
        print("testcase_001第三方分享回调")

        member_id = "960"
        payload = {'platform':'facebook','post_id':6523}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------分享app----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_002(self):
        sheet_index = 6
        row = 9
        print("testcase_002分享app：")
        member_id = "960"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
