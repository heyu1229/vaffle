# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc,xlrd
import json
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests


#---------------举报动态----------------------
class PostsReport(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------举报动态----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 7
        print("testcase_001举报动态：")

        payload ={"post_id": 428819,"reason_id": "1"}
        member_id = "960"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        try:
            self.assertEqual(10000, result["code"])
            print("code返回值：10000")
        except:
            self.assertEqual(10014, result["code"])
            print("code返回值：10014")

if __name__=="__main__":
    unittest.main()