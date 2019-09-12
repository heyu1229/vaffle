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

#---------------Q/A的关注和取消关注----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------Q/A的关注----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 26
        print("testcase_001 Q/A的关注：")

        payload = {"question_id": 174470,"follow_state": 1}
        member_id="960"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # -----------------Q/A的取消关注----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 27
        print("testcase_002 Q/A的取消关注：")

        payload = {"question_id": 174470, "follow_state":0}
        member_id="960"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()