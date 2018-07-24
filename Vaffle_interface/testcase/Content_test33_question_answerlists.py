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
        row = 82
        print("testcase_001 用户对于Q／A的回答列表第一页数据：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = { "content": "接口在" + date + "测试发布Q/A","category":"qa"}
        member_id1 = "748"
        urlpart = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)
        print(result1)
        global question_id
        question_id = result1["data"]["question_id"]
        print(question_id)

        # 调用QA回答接口发送一条回答
        payload2 = {"question_id": question_id, "content": "接口在" + date + "测试回答Q/A"}
        member_id2 = "744"
        urlpart2 = '/answer/publish'
        result2 = self.r.interface_requests_data(member_id2, urlpart2, payload2)
        result2 = self.r.interface_requests_data('745', urlpart2, payload2)
        result2 = self.r.interface_requests_data('746', urlpart2, payload2)
        result2 = self.r.interface_requests_data('747', urlpart2, payload2)
        result2 = self.r.interface_requests_data('748', urlpart2, payload2)
        result2 = self.r.interface_requests_data('749', urlpart2, payload2)
        result2 = self.r.interface_requests_data('750', urlpart2, payload2)
        result2 = self.r.interface_requests_data('751', urlpart2, payload2)
        result2 = self.r.interface_requests_data('752', urlpart2, payload2)
        result2 = self.r.interface_requests_data('753', urlpart2, payload2)
        result2 = self.r.interface_requests_data('754', urlpart2, payload2)


        payload = {"question_id": question_id,"page": 1}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        global last_answer_id
        last_answer_id=result["data"]["last_answer_id"]
        print(last_answer_id)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------用户对于Q／A的回答列表第二页数据-----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 83
        print("testcase_002 用户对于Q／A的回答列表二页数据：")
        member_id = "744"
        payload={"question_id":question_id,"page":2,"last_answer_id":last_answer_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------用户744的Q／A回答列表----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 84
        print("testcase_002 用户744的Q／A回答列表：")
        member_id = "744"
        payload={"question_id":question_id,"page":1,"member_id":member_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()