# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc
import time,sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------用户每日签到---------------------------
class Signboard(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------用户每日签到----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 25
        print("testcase001 用户简介资料更新：")
        result = self.requests.interface_requests2(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


if __name__ == '__main__':
    unittest.main()