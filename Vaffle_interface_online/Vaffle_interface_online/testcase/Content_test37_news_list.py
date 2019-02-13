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

#---------------首页news列表和用户中心的review列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------首页news列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 90
        print("testcase_001 首页news列表第一页数据：")

        member_id = "744"
        result = self.r.interface_requests(member_id, sheet_index, row)
        list = result['data']['list']
        global last_id
        last_id = list[9]['post_id']
        print(last_id)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

 #-----------------首页news列表第二页数据----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 91
        print("testcase_002 首页news列表第二页数据：")

        member_id = "744"
        payload = {"category": "all", "last_id": last_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------用户中心的review列表第一页数据----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 92
        print("testcase_003 用户中心的review列表第一页数据：")

        member_id = "744"
        result = self.r.interface_requests(member_id, sheet_index, row)
        post_list = result['data']['list']

 #-----------------用户中心的review列表第二页数据----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 93
        print("testcase_004 用户中心的review列表第二页数据：")

        member_id = "744"
        payload = {"category": "mine", "last_id": 12451}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()