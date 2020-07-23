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

#---------------店铺媒体资源列表（网友、官方）----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------店铺媒体资源列表--网友----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 4
        member_id='744'
        print ("testcase_001店铺媒体资源列表--网友:")

        result = self.r.interface_requests(member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------店铺媒体资源列表--官方----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 5
        member_id='744'
        print ("testcase_001店铺媒体资源列表--官方:")

        result = self.r.interface_requests(member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------店铺媒体资源列表--视频----------------------------------
    def testcase_003(self):
        sheet_index = 12
        row = 6
        member_id='744'
        print ("testcase_001店铺媒体资源列表--视频:")

        result = self.r.interface_requests(member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()