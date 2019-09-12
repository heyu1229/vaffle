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

#---------------活动状态----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

 # -----------------活动状态----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 26
        print("testcase_001 活动状态：")

        member_id = '6f64a13d-3fd0-48e2-ad5b-5eb61638cca2'
        result=self.r.interface_requests_apitest2(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()