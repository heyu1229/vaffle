# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc

import time,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------用户每日签到---------------------------
class Signboard(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------用户每日签到----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 96
        print("testcase001 用户简介资料更新：")
        result = self.requests.interface_requests2(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


if __name__ == '__main__':
    unittest.main()