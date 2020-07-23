# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc
import json

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
#from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------【营救电子烟】 领取任务机会----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

 # -----------------领取publish_post任务机会----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 28
        print("testcase_001 领取publish_post任务机会：")

        member_id = '07ce98c4-b156-4719-b30d-9d0acdab868c'
        payload = {"task_type":"publish_post"}
        result=self.r.interface_requests_payload_apitest2(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

 # -----------------领取attention任务机会----------------------------------
    def testcase_002(self):
        sheet_index = 3
        row = 29
        print("testcase_002 领取attention任务机会：")

        member_id = '07ce98c4-b156-4719-b30d-9d0acdab868c'
        payload = {"task_type":"attention"}
        result=self.r.interface_requests_payload_apitest2(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

 # -----------------领取praise_post任务机会----------------------------------
    def testcase_003(self):
        sheet_index = 3
        row = 30
        print("testcase_003 领取praise_post任务机会：")

        member_id = '07ce98c4-b156-4719-b30d-9d0acdab868c'
        payload = {"task_type":"praise_post"}
        result=self.r.interface_requests_payload_apitest2(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

 # -----------------领取read_hotnews任务机会----------------------------------
    def testcase_004(self):
        sheet_index = 3
        row = 31
        print("testcase_004 领取read_hotnews任务机会：")

        member_id = '07ce98c4-b156-4719-b30d-9d0acdab868c'
        payload = {"task_type":"read_hotnews"}
        result=self.r.interface_requests_payload_apitest2(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()