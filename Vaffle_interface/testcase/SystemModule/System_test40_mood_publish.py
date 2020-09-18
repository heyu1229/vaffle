# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#---------------心情打卡发布---------------------
class web_subscribe_info(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    def testcase_001(self):
        sheet_index = 3
        row = 51
        payload = {"pid": 18, "tid": 2892548071, "content": "aaaa"}
        result=self.requests.interface_requests_payload(self.member_uuid, sheet_index, row,payload)
        self.assertEqual(30102, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()