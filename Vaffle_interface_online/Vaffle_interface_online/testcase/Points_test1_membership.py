# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------积分等级首页----------------------
class Membership(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------积分等级首页----------------------------------
    def testcase_001(self):
        sheet_index =8
        row = 1
        print("testcase001 积分等级首页：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()