# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc
import xlrd
import json
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------通知消息列表----------------------------
class MessageceNotice(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------通知消息列表----------------------------------
    def testcase_001(self):
        sheet_index = 5
        row = 2
        print("testcase_001通知消息列表：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()