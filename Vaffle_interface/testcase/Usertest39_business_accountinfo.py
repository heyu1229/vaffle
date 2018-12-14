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

#---------------获取商业级用户的登录信息----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()
       self.member_id = '745'

    #-----------------获取商业级用户的登录信息----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 109
        print("testcase_001获取商业级用户的登录信息：")
        payload = {"normal_member_id":745,"target_role":10394,"fcm_token":"fcm_token"}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()