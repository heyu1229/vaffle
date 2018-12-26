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
        sheet_index = 12
        row = 27
        member_id='746'
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
        sheet_index = 12
        row = 40
        member_id='746'
        print ("testcase_002普通用户认领店铺:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "接口测试店铺"+date, "nation": "china","city": "shangai","address": "qilianshanlu",
                   "first_name": "first_name","last_name": "last_name","img_card_front":"posts/1512710644871_767_android.jpg",
                   "img_card_back":"posts/1512710644871_767_android.jpg","img_license":"posts/1512710644871_767_android.jpg",
                   "is_boss":1,"apply_shop_id":29388,"normal_member_id":746}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10095, result['code'])
            print("code返回值：10095")

    #----------------管理员身份登录后，认领另一个已经是管理员的店铺----------------------------------
    def testcase_003(self):
        sheet_index = 12
        row = 41
        member_id='10394'
        print ("testcase_003管理员身份登录后，认领另一个已经是管理员的店铺:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "接口测试店铺"+date, "nation": "china","city": "shangai","address": "qilianshanlu",
                   "first_name": "first_name","last_name": "last_name","img_card_front":"posts/1512710644871_767_android.jpg",
                   "img_card_back":"posts/1512710644871_767_android.jpg","img_license":"posts/1512710644871_767_android.jpg",
                   "is_boss":1,"apply_shop_id":53951,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10095, result['code'])
            print("code返回值：10095")

    #----------------管理员认领店铺----------------------------------
    def testcase_004(self):
        sheet_index = 12
        row = 42
        member_id='760'
        print ("testcase_004管理员认领店铺:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "queen test 001", "nation": "china","city": "shangai","address": "永登路",
                   "first_name": "Yukon","last_name": "yu","img_card_front":"posts/1512710644871_767_android.jpg",
                   "img_card_back":"posts/1512710644871_767_android.jpg","img_license":"posts/1512710644871_767_android.jpg",
                   "is_boss":1,"apply_shop_id":53977,"normal_member_id":member_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10095, result['code'])
            print("code返回值：10095")

if __name__ == "__main__":
    unittest.main()