# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------签到 - 用户补签提示----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------签到 - 用户补签提示----------------------------------
    #1 已经签到 2 ，漏签， 3，当天未签到 4 未来未签到
    def testcase_001(self):
        sheet_index = 0
        row = 47
        print("testcase_001签到 用户补签提示：")
        payload = {'date': '2020-07-29', 'sign_status': '1'}
        result = self.requests.interface_requests_payload(self.member_uuid,sheet_index,row,payload)
        # result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()