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

#---------------单条QA的详情---------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------单条QA的详情----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 81
        print("testcase_001 单条QA的详情：")

        # 调用发布接口发送一条动态，获取question_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # payload1 = { "content": "接口在" + date + "测试发布Q/A","category":"qa"}
        # member_id1 = "748"
        # urlpart1 = '/posts/publish'
        # result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        # global question_id
        # question_id = result1["data"]["question_id"]
        # print(question_id)

        question_id="19183"
        payload = {"question_id": question_id}
        member_id = "744"
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()