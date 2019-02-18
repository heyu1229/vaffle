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

#---------------申请成为店铺店主----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------普通用户申请成为店铺店主----------------------------------
    def testcase_001(self):
        sheet_index = 11
        row = 21
        member_id='960'
        print ("testcase_001普通用户申请成为店铺店主:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "接口测试店铺"+date, "nation": "china","city": "shangai","address": "qilianshanlu",
                   "first_name": "first_name","last_name": "last_name","img_card_front":"posts/1512710644871_767_android.jpg",
                   "img_card_back":"posts/1512710644871_767_android.jpg","img_license":"posts/1512710644871_767_android.jpg",
                   "is_boss":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10095, result['code'])
            print("code返回值：10095")

    #-----------------普通用户认领店铺----------------------------------
    def testcase_002(self):
        sheet_index = 11
        row = 22
        member_id='960'
        print ("testcase_002普通用户认领店铺:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "接口测试店铺"+date, "nation": "china","city": "shangai","address": "qilianshanlu",
                   "first_name": "first_name","last_name": "last_name","img_card_front":"posts/1512710644871_767_android.jpg",
                   "img_card_back":"posts/1512710644871_767_android.jpg","img_license":"posts/1512710644871_767_android.jpg",
                   "is_boss":1,"apply_shop_id":29388,"normal_member_id":960}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10095, result['code'])
            print("code返回值：10095")

if __name__ == "__main__":
    unittest.main()