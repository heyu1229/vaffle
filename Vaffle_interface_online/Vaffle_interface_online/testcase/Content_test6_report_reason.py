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

#---------------举报动态原因----------------------
class ReportReason(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------举报动态原因----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 16
        print("testcase_001举报动态原因：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()