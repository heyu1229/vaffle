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

#---------------钱包 - 删除可提现账户----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()
       self.member_id = '10394'

    #-----------------钱包 - 删除可提现账户----------------------------------
    def testcase_001(self):
        sheet_index = 13
        row = 9
        print("testcase_001钱包 - 删除可提现账户：")

        # 调用提现账户添加接口获取account_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        urlpart1 = '/wallet/account/add'
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"account": date, "first_name": "yu", "last_name": "qin"}
        result1 = self.r.interface_requests_data(self.member_id, urlpart1, payload1)

        urlpart2='/wallet/account/lists'
        payload2={}
        result2 = self.r.interface_requests_data(self.member_id, urlpart2, payload2)
        list = result2["data"]["list"]
        account_id = list[0]["id"]
        print("account_id=",account_id)

        payload={"account_id":account_id}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()