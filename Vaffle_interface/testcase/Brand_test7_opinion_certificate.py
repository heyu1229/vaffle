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

#---------------想法认可、想法取消----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------想法认可、想法取消----------------------------------

    def testcase_001(self):
        sheet_index = 11
        row = 7
        print ("testcase_001想法认可:")

        # 调用想法管理列表，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"page": 1, "normal_member_id": 745}
        member_id1 = "34791"
        urlpart1 = '/opinion/manage'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        print(result1)
        list = result1["data"]["list"]
        post_id=list[0]["post_id"]
        print("post_id=",post_id)

        member_id = '34791'
        payload = {"post_id": post_id, "state": 1,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------想法取消认可----------------------------------
    def testcase_002(self):
        sheet_index = 11
        row = 8
        print ("testcase_002想法取消认可:")

        # 调用想法管理列表，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"page": 1, "normal_member_id": 745}
        member_id1 = "34791"
        urlpart1 = '/opinion/manage'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        print(result1)
        list = result1["data"]["list"]
        post_id=list[0]["post_id"]
        print("post_id=",post_id)

        member_id = '34791'
        payload = {"post_id": post_id, "state": 0 ,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()
