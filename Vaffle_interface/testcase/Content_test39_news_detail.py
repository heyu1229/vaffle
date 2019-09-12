# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import json
import time

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------对news详情----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------news详情（review类型)----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 96
        print("testcase_001 news详情（review类型)：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = { "content": "接口在" + date + "测试发布review","category":"review","review_title":"review_title","review_product":"review_product","review_type":"review_type"}
        member_id1 = "744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        print(result1)
        global post_id
        post_id = result1["data"]["post_id"]
        print(post_id)

        payload = {"category": "review", "post_id": post_id}
        member_id = "744"
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # -----------------news详情（news类型)----------------------------------

    def testcase_002(self):
        sheet_index = 1
        row = 97
        print("testcase_002 news详情（news类型)：")

        payload = {"category": "news", "post_id": "41931"}
        member_id = "744"
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # -----------------hotnews详情（news类型)----------------------------------

    def testcase_003(self):
        sheet_index = 1
        row = 110
        print("testcase_003news详情（hotnews类型)：")

        payload = {"category": "news", "post_id": "41931"}
        member_id = "744"
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
if __name__ == "__main__":
    unittest.main()