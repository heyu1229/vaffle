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

#---------------QA回答的评论列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------QA回答的评论列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 85
        print("testcase_001 QA回答的评论列表第一页数据：")

        payload = {"answer_id": 101368,"page": 1}
        member_id="960"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------用户对于Q／A的回答列表第二页数据-----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 86
        print("testcase_002 用户对于Q／A的回答列表二页数据：")
        member_id = "744"
        payload = {"answer_id": answer_id, "page": 2, "comment_id_past": comment_id_past}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------评论置顶-----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 101
        print("testcase_003 评论置顶：")
        member_id = "744"
        payload = {"answer_id": answer_id, "page": 1, "comment_id": comment_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # 回答成功后，删除回答，不然后面的接口不能再回答这个问题
        payload1 = {"answer_id": answer_id}
        member_id1 = "744"
        urlpart = '/answer/delete'
        result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)

if __name__ == "__main__":
    unittest.main()