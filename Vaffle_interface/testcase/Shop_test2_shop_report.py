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

#---------------举报商户----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.requests = FuncRequests ()
       self.member_id = 'none'

    #-----------------举报商户成功----------------------------------
    def testcase_001(self):
        #先注册新用户
        sheet_index =0
        row = 12
        print("testcase001 用户注册成功:")
        nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        nickname = 'heyu'+nowTime
        email = 'heyu'+nowTime+'@qq.com'
        print(email)
        payload = {'email': email,'password': 'aaa111','displayname': 'heyu','nickname': nickname,'equipment_number': 'PE-TL10',}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.member_id=str(result["data"]["member_id"])
        print(self.member_id)
        sheet_index = 12
        row = 2
        print ("testcase_001举报商户:")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------重复举报商户----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 3
        self.member_id = "744"
        print ("testcase_002重复举报商户:")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10014, result['code'])
        print("code返回值：10014")
        print("msg：You are reported.")

if __name__ == "__main__":
    unittest.main()