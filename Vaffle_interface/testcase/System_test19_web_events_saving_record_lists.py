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

#---------------【营救电子烟】 跑马灯/获奖 记录列表---------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

 # -----------------跑马灯记录列表----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 32
        print("testcase_001 跑马灯记录列表：")

        member_id = '07ce98c4-b156-4719-b30d-9d0acdab868c'
        result=self.r.interface_requests_apitest2(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()