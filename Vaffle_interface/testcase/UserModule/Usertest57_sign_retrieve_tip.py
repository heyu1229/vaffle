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

#---------------签到 - 用户补签提示----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.requests = FuncRequests ()
        self.member_id = '959'

    #-----------------签到 - 用户补签提示----------------------------------
    #1 已经签到 2 ，漏签， 3，当天未签到 4 未来未签到
    def testcase_001(self):
        #-----用户注册-----
        self.member_id ='959'
        sheet_index = 0
        row = 138
        print("testcase_001签到 用户补签提示：")
        payload = {'date': '2019-01-01', 'sign_status': '1'}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        # result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()