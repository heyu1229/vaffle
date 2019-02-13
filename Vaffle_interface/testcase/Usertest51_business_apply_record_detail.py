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

#---------------查看申请记录的详情信息----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()
       self.member_id = '746'

    #-----------------申请店铺管理者的详情信息----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 129

        s = "select a.id from vape_business_log a, vape_shop_keeper_apply b where a.pri_id=b.id and b.member_id=746"
        id = self.r.sql_vaffle_post(s)
        print('apply_id=', id)
        apply_id = id['id']
        print("testcase_001 申请店铺管理者的详情信息：")
        payload = {"category":1,"id":apply_id}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------申请品牌管理者的详情信息----------------------------------
    def testcase_002(self):
        sheet_index = 0
        row = 140
        self.member_id = '745'
        s = "select a.id from vape_business_log a, vape_brand_keeper_apply b where a.pri_id=b.id and b.member_id=745"
        id = self.r.sql_vaffle_post(s)
        print('apply_id=', id)
        apply_id = id['id']
        print("testcase_002 申请品牌管理者的详情信息：")
        payload = {"category":3,"id":apply_id}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------提交修改品牌资料的详情信息----------------------------------
    def testcase_003(self):
        sheet_index = 0
        row = 141
        self.member_id = '34791'
        s = "select a.id from vape_business_log a, vape_enterbrand_audit b where a.pri_id=b.id and b.member_id=34791"
        id = self.r.sql_vaffle_post(s)
        print('apply_id=', id)
        apply_id = id['id']
        print("testcase_003 提交修改品牌资料的详情信息：")
        payload = {"category":4,"id":apply_id}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------查看申请记录的详情信息----------------------------------
    def testcase_004(self):
        sheet_index = 0
        row = 142
        self.member_id = '10394'
        s = "select a.id from vape_business_log a, vape_shops_audit b where a.pri_id=b.id and b.member_id=10394"
        id = self.r.sql_vaffle_post(s)
        print('apply_id=', id)
        apply_id = id['id']
        print("testcase_004 修改店铺资料的详情信息：")
        payload = {"category":5,"id":apply_id}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()