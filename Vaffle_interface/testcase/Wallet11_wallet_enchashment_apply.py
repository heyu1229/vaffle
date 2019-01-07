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

#---------------钱包 - 发起提现申请----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()
       self.member_id = '10394'

    #-----------------钱包 - 发起提现申请----------------------------------
    def testcase_001(self):
        s = "delete from vape_reflect_record where member_id='10394'"
        execute_sql = self.r.sql_vaffle(s)
        s1="update vape_wallet set balance=100,frozen_money=0 where member_id='10394'"
        execute_sql1 = self.r.sql_vaffle(s1)
        #1.因为提现最小金额是50，所以要先去数据库将balane改成比frozen_money大50才能执行该用例
        #2.因为一个月只能提现一次，所以要先删除数据库中表vape_reflect_record中该用户的当月提现记录
        sheet_index = 13
        row = 13
        print("testcase_001钱包 - 发起提现申请：")

        payload={"account":"2018-12-06 13:11:11","money":"50"}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------钱包 - 提现金额不能小于50----------------------------------
    def testcase_002(self):
        #因为提现最小金额是50，所以要先去数据库将可提现金额手动改成大于50才能执行该用例
        s="delete from vape_reflect_record where member_id='10394'"
        execute_sql = self.r.sql_vaffle(s)
        sheet_index = 13
        row = 14
        print("testcase_002提现金额不能小于50：")

        payload={"account":"2018-12-06 13:11:11","money":"0.01"}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10110, result['code'])
        print("code返回值：10110")

    #-----------------钱包 - 提现金额不能大于实际可提现金额----------------------------------
    def testcase_003(self):
        #因为提现最小金额是50，所以要先去数据库将可提现金额手动改成大于50才能执行该用例
        s="delete from vape_reflect_record where member_id='10394'"
        execute_sql = self.r.sql_vaffle(s)
        sheet_index = 13
        row = 15
        print("testcase_003提现金额不能大于实际可提现金额：")

        payload={"account":"2018-12-06 13:11:11","money":"100000"}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10109, result['code'])
        print("code返回值：10109")

if __name__ == "__main__":
    unittest.main()