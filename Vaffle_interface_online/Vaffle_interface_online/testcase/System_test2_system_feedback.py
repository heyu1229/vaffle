# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import json
import time

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------用户反馈----------------------
class System_feedback(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------用户反馈----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 2
        print("testcase_001用户反馈：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"content": "接口在"+date+"测试用户反馈","email": "921467314@qq.com"}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------用户反馈空内容----------------------------------
    def testcase_002(self):
        sheet_index = 3
        row = 3
        print("testcase_002用户反馈空内容：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"content": "","email": "921467314@qq.com"}
        # 获取token值
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

if __name__=="__main__":
    unittest.main()