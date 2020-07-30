# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------添加收货地址----------------------
class Address_add(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------添加收货地址----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 30
        print("testcase_001添加收货地址：")
        date = int(time.time())
        payload = {'firstname': 'Yu' ,'lastname':date ,'phone':'15800110123','country':'China','state':'shanghai','city':'shanghai','street':'No.1611,zhennan road','zip_code':'210110'}
        result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()