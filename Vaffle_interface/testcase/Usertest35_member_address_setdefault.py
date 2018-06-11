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

#---------------设置默认地址----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------设置默认地址----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 104
        print("testcase_001设置默认地址：")
        # 先调用添加收获地址借口哦添加一个地址，然后进行设置
        date = int(time.time())
        payload = {'firstname': 'Yu' ,'lastname':date ,'phone':'15800110123','country':'China','state':'shanghai','city':'shanghai','street':'No.1611,zhennan road','zip_code':'210110'}
        member_id = "744"
        urlpart = '/member/address/add'
        result1 = self.r.interface_requests_data(member_id, urlpart, payload)
        address_id = result1['data']['address_id']

        payload = {'address_id':address_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()