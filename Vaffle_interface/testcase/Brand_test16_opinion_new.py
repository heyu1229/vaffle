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

#---------------最新想法列表---------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------品牌下的最新想法列表第1页数据----------------------------------

    def testcase_001(self):
        sheet_index = 11
        row = 22
        print ("testcase_001品牌下的最新想法列表第1页数据:")

        member_id = '980'
        payload = {"page": 1,"brand_id":1,"topic_id":0}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        list=result["data"]["list"]
        global last_id
        last_id = list[9]["post_id"]
        print("last_id=",last_id)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------品牌下的最新想法列表第2页数据----------------------------------

    def testcase_002(self):
        sheet_index = 11
        row = 23
        print ("testcase_002品牌下的最新想法列表第2页数据:")

        member_id = '980'
        payload = {"page": 2,"last_id":last_id,"brand_id":1,"topic_id":0}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

   #-----------------话题下的最新想法列表第1页数据----------------------------------

    def testcase_003(self):
        sheet_index = 11
        row = 24
        print ("testcase_003话题下的最新想法列表第1页数据:")

        member_id = '980'
        payload = {"page": 1,"brand_id":0,"topic_id":40}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        list=result["data"]["list"]
        global last_id1
        last_id1 = list[9]["post_id"]
        print("last_id=",last_id1)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------话题下的最新想法列表第2页数据----------------------------------

    def testcase_004(self):
        sheet_index = 11
        row = 25
        print ("testcase_004话题下的最新想法列表第2页数据:")

        member_id = '980'
        payload = {"page": 2,"last_id":last_id1,"brand_id":0,"topic_id":40}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
