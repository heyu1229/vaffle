# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#---------------删除收货地址----------------------
class Address_delete(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------删除收货地址----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 32
        print("testcase_001删除收货地址：")
        # 先调用添加收获地址借口哦添加一个地址，然后进行删除
        date = int(time.time())
        payload = {'firstname': 'Yu' ,'lastname':date ,'phone':'15800110123','country':'China','state':'shanghai','city':'shanghai','street':'No.1611,zhennan road','zip_code':'210110'}
        member_id = "744"
        urlpart = '/member/address/add'
        result1 = self.requests.interface_requests_data(self.member_uuid, urlpart, payload)
        address_id = result1['data']['address_id']

        payload = {'address_id':address_id}
        result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()