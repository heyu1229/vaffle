# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc
import time,sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#---------------更新用户的Google fcm token----------------------
class FcmToken(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------更新用户的Google fcm token----------------------------------

    def testcase_001(self):
        sheet_index =0
        row = 23
        print("testcase001 更新用户的Google fcmtoken：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()