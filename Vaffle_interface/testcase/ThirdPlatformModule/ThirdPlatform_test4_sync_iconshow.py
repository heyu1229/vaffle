# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------发布时第三方平台图标显示【POST】----------------------
class Sync_iconshow(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()
        self.member_id ='none'

    def testcase_001(self):
        sheet_index = 6
        row = 11
        print("testcase_001发布时第三方平台图标显示")

        payload = {}
        result=self.r.interface_requests_payload(self.member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()
