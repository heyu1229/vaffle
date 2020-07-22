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
#from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------QA推荐答题列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------QA推荐答题列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 114
        print("testcase_001 QA推荐答题列表：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload={}
        result = self.r.interface_requests_payload(member_id, sheet_index, row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()