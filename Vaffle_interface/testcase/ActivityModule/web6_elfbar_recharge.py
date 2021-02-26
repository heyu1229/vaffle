'''
@create : lisa
@file :web5_elfbar_reserve.py
@Date :2021/2/26
@desc :

'''
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd

from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#---------------【H5】elfbar活动-兑换【POST】--------------------
class web_elfbar_recharge(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()


    def testcase_001(self):
        sheet_index = 16
        row = 6
        payload ={"shopId":"123","code":"919850"}
        result = self.requests.interface_requests_payload(self.member_uuid,sheet_index,row,payload)
        self.assertEqual(10009, result['code'])
        print("code返回值：10009")

if __name__ == "__main__":
    unittest.main()