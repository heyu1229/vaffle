#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc,xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------动态点赞/取消点赞----------------------
class Praise(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()
        # 获取版本
        self.version = Version().test_version()
        self.url = Url().test_url()

    #-----------------动态点赞/取消点赞----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 5
        print("testcase_001动态点赞/取消点赞：")

        # 调用posts/lists接口获取post_id
        payload1 = {"type": "post", "page": 1}
        member_id1 = "960"
        urlpart='/posts/lists'
        result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)
        list = result1["data"]["list"]
        post_id = list[0]["post_id"]
        print("post_id:",post_id)

        payload ={"post_id": post_id,"praise_state":1}
        member_id = "960"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
