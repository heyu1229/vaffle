# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------签到 - 用户签到列表----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.requests = FuncRequests ()
        self.member_id = '959'

    #-----------------签到 - 用户签到列表 ----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 37
        print("testcase_001签到 用户签到列表：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()