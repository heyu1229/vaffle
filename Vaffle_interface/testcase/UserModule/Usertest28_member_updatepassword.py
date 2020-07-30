# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc
import time,sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------用户修改密码---------------------------
from Vaffle_interface.public_1.get_version import Version


class Update_password(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    # -----------------用户修改密码----------------------------------

    def testcase_001(self):
        sheet_index = 0
        row = 28
        print("testcase_001修改密码111111改为222222:")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    def testcase_002(self):
        sheet_index = 0
        row = 29
        print("testcase_002修改密码222222改为111111")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


if __name__ == '__main__':
    unittest.main()