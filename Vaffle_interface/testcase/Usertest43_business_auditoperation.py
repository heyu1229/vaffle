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

#---------------店铺品牌管理员审核操作----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()


    #-----------------店铺管理员审核操作----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 116

        s = "select id from vape_shop_keeper_apply where shop_id=29388 and status=1 or status=2"
        id = self.r.sql_vaffle_post(s)
        apply_id = id['id']
        print('apply_id=', apply_id)
        print("testcase_001店铺管理员审核操作：")
        self.member_id = '10394'
        payload = {"normal_member_id":745,"type":"shop","apply_id":apply_id,"action":"pass","is_boss":"2"}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------品牌管理员审核操作----------------------------------
    def testcase_002(self):
        sheet_index = 0
        row = 117

        s = "select id from vape_brand_keeper_apply where brand_id=1 and status=1 or status=2"
        id = self.r.sql_vaffle_post(s)
        apply_id = id['id']
        print('apply_id=', apply_id)
        self.member_id = '34791'
        print("testcase_002品牌管理员审核操作：")
        payload = {"normal_member_id": 745, "type": "brand", "apply_id": apply_id, "action": "pass", "is_boss": "2"}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()