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

#---------------产品 - 新增 产品----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------产品 - 新增 产品----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 33
        member_id='10394'
        print ("testcase_001新增产品:")

        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        print("images=",images)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "autotest"+date,"description":"description"+date, "total": 3,"images": images,
                   "shop_id":29388,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

  #-----------------产品 - 其他管理员新增产品----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 43
        member_id='34791'
        print ("testcase_002其他管理员新增产品:")

        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        print("images=",images)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "autotest"+date,"description":"description"+date, "total": 3,"images": images,
                   "shop_id":29388,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()