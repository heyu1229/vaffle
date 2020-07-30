# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------用户退出接口---------------------------
class Logout(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------用户退出----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 22
        print("testcase001 用户退出登录：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('logout success', result['msg'])
        print("msg返回值：logout success")

if __name__ == '__main__':
    unittest.main()