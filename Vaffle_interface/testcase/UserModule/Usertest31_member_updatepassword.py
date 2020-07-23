# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc

import time,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------用户修改密码---------------------------
class Update_password(unittest.TestCase):

    def setUp(self):
        self.member_id = '1455'
        self.requests = FuncRequests()
    # -----------------用户修改密码----------------------------------

    def testcase_001(self):
        sheet_index = 0
        row = 99
        print("testcase_001修改密码111111改为222222:")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    def testcase_002(self):
        sheet_index = 0
        row = 100
        print("testcase_002密码改回222222改为111111:")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


if __name__ == '__main__':
    unittest.main()