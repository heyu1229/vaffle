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

#---------------申请品牌管理者---------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------申请品牌管理者----------------------------------
    def testcase_001(self):
        sheet_index = 11
        row = 29
        print ("testcase_001申请品牌管理者:")

        member_id = '745'
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "接口测试品牌"+date, "nation": "china", "city": "shangai", "address": "qilianshanlu",
                   "first_name": "first_name", "last_name": "last_name",
                   "img_card_front": "posts/1512710644871_767_android.jpg",
                   "img_card_back": "posts/1512710644871_767_android.jpg",
                   "img_license": "posts/1512710644871_767_android.jpg",
                   "is_boss": 1,"phone":"18812341234","email":"email@qq.com","normal_member_id":member_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10095, result['code'])
            print("code返回值：10095")

    #-----------------认领品牌管理者----------------------------------
    def testcase_002(self):
        sheet_index = 11
        row = 30
        print ("testcase_002认领品牌管理者:")

        member_id = '748'
        payload = {"name": "接口测试品牌", "nation": "china", "city": "shangai", "address": "qilianshanlu",
                   "first_name": "first_name", "last_name": "last_name",
                   "img_card_front": "posts/1512710644871_767_android.jpg",
                   "img_card_back": "posts/1512710644871_767_android.jpg",
                   "img_license": "posts/1512710644871_767_android.jpg",
                   "is_boss": 1,"phone":"18812341234","email":"email@qq.com","normal_member_id":member_id,
                   "apply_brand_id":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10116, result['code'])
            print("code返回值：10116")

    #-----------------不能认领已经是管理者的品牌----------------------------------
    def testcase_003(self):
        sheet_index = 11
        row = 31
        print ("testcase_003不能认领已经是管理者的品牌:")

        member_id = '745'
        payload = {"name": "接口测试品牌", "nation": "china", "city": "shangai", "address": "qilianshanlu",
                   "first_name": "first_name", "last_name": "last_name",
                   "img_card_front": "posts/1512710644871_767_android.jpg",
                   "img_card_back": "posts/1512710644871_767_android.jpg",
                   "img_license": "posts/1512710644871_767_android.jpg",
                   "is_boss": 1,"phone":"18812341234","email":"email@qq.com","normal_member_id":member_id,
                   "apply_brand_id":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10120, result['code'])
            print("code返回值：10120")

    #-----------------管理员身份登录后，不能认领另一个已经是管理员的品牌----------------------------------
    def testcase_004(self):
        sheet_index = 11
        row = 32
        print ("testcase_004管理员身份登录后，不能认领另一个已经是管理员的品牌:")

        member_id = '34791'
        payload = {"name": "接口测试品牌", "nation": "china", "city": "shangai", "address": "qilianshanlu",
                   "first_name": "first_name", "last_name": "last_name",
                   "img_card_front": "posts/1512710644871_767_android.jpg",
                   "img_card_back": "posts/1512710644871_767_android.jpg",
                   "img_license": "posts/1512710644871_767_android.jpg",
                   "is_boss": 1,"phone":"18812341234","email":"email@qq.com","normal_member_id":745,
                   "apply_brand_id":3}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10120, result['code'])
            print("code返回值：10120")

if __name__ == "__main__":
    unittest.main()