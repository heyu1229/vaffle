#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc,xlrd
import json,time
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests
#---------------discover video列表----------------------
class List(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()


    #-----------------首页动态列表post 第1页----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 3
        print("testcase_001首页动态列表post 第1页:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        post_list = result['data']['list']
        global last_id
        last_id = post_list[9]['post_id']

    #-----------------首页动态列表reveal 第1页---------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 4
        print("testcase_002首页动态列表reveal 第1页:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


   #-----------------首页动态列表post 第2页----------------------------------
    def testcase_003(self):

        sheet_index = 1
        row = 5
        print("testcase_003页动态列表post 第2页:")
        member_id="744"
        print('last_id: ',last_id)
        #再根据last_id获得第二页数据
        payload = {'type':'post','page':2,'last_id':last_id}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------首页动态列表type不存在----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 7
        print("testcase_004首页动态列表type不存在:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

    #-----------------首页动态列表hotnews 第1页---------------------------------
    def testcase_005(self):
        sheet_index = 1
        row = 109
        print("testcase_005首页动态列表hotnews 第1页:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()