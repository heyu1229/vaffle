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

#---------------用户对于Q／A的回答列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------用户对于Q／A的回答列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 36
        print("testcase_001 用户对于Q／A的回答列表第一页数据：")

        payload = {"question_id": 173553,"page": 1}
        member_id="960"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        global last_answer_id
        last_answer_id=result["data"]["last_answer_id"]
        print(last_answer_id)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------用户对于Q／A的回答列表第二页数据-----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 37
        print("testcase_002 用户对于Q／A的回答列表二页数据：")
        member_id = "744"
        payload={"question_id":173553,"page":2,"last_answer_id":last_answer_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------用户744的Q／A回答列表----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 38
        print("testcase_003 用户960的Q／A回答列表：")
        member_id = "960"
        payload={"question_id":173553,"page":1,"member_id":member_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()