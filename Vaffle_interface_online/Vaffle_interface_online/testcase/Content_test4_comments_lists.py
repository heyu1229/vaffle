# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc,xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------评论列表----------------------
class CommentsLists(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------评论列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 6
        print("testcase_001评论列表:")

        payload = {'post_id': 428819, 'page': 1}
        member_id = "960"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()