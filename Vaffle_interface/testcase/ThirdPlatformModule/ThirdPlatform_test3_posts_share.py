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
        row = 7
        print("testcase_001第三方分享回调")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布纯文字"}
        member_id = "744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        post_id = result1["data"]["post_id"]
        print(post_id)

        #调用第三方分享回调接口
        payload = {'platform':'facebook','post_id':post_id}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------不支持的第三方----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_002(self):
        sheet_index = 6
        row = 8
        print("testcase_002不支持的第三方")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------分享app----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_003(self):
        sheet_index = 6
        row = 9
        print("testcase_003分享app：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
