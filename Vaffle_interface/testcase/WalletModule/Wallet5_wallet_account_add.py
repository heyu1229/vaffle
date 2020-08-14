# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys

#------------------------钱包 - 提现记录---------------------------
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url


class wallet_income(unittest.TestCase):

    def setUp(self):
        self.member_uuid = "9ccc4119-f04d-43b5-9c0f-c3cf679fe4c9"
        self.requests = FuncRequests()


    #-----------------钱包 - 提现账户添加----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 5
        print("testcase_001钱包 - 提现账户添加：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"account":date,"first_name":"yu","last_name":"qin"}
        result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()