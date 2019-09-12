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

#---------------（品牌）话题列表 - 用户个人中心---------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------话题列表 - 用户个人中心----------------------------------

    def testcase_001(self):
        sheet_index = 10
        row = 8
        print ("testcase_001话题列表 - 用户个人中心:")

        member_id = '960'
        payload = {"member_id":member_id,"page":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------话题列表 - 用户角度----------------------------------

    def testcase_002(self):
        sheet_index = 10
        row = 9
        print ("testcase_002话题列表 - 用户角度:")

        member_id = '960'
        payload = {"brand_id": 14,"page":1,"page_size":20}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


    #-----------------话题列表 - 管理员角度----------------------------------

    def testcase_003(self):
        sheet_index = 10
        row = 10
        print ("testcase_003话题列表 - 管理员角度:")

        member_id = '66710'
        payload = {"brand_id": 16,"page":1,"admin_view":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()