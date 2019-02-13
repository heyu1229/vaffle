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

#---------------检测用户是否设置 （第三方） 登录密码----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.requests = FuncRequests ()
        self.member_id = '745'

    #-------------------非第三方平台账户--------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 143
        print("testcase_001 非第三方平台账户：")
        payload={"normal_member_id":745}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

  #-------------------第三方平台账户--------------------------------
    def testcase_002(self):
        sheet_index = 0
        row = 144
        print("testcase_002 第三方平台账户：")
        payload={"normal_member_id":1295}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()