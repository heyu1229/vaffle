# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------设置默认地址----------------------
class Address_setdefault(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------设置默认地址----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 33
        print("testcase_001设置默认地址：")
        # 先调用添加收获地址借口哦添加一个地址，然后进行设置
        date = int(time.time())
        payload = {'firstname': 'Yu' ,'lastname':date ,'phone':'15800110123','country':'China','state':'shanghai','city':'shanghai','street':'No.1611,zhennan road','zip_code':'210110'}
        urlpart = '/member/address/add'
        result1 = self.requests.interface_requests_data(self.member_uuid, urlpart, payload)
        address_id = result1['data']['address_id']

        payload = {'address_id':address_id}
        result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()