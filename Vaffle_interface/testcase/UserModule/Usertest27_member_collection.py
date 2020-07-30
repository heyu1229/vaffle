# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc

import time,sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------用户收藏的post列表---------------------------
class Update_background(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    # -----------------用户收藏的post列表----------------------------------

    def testcase_001(self):
        sheet_index = 0
        row = 27
        print("testcase_001用户收藏的post列表:")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


if __name__ == '__main__':
    unittest.main()