# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc

import time,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------更新用户中心封面---------------------------
class Update_background(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    # -----------------成功更新背景图----------------------------------

    def testcase_001(self):
        sheet_index = 0
        row = 97
        print("testcase_001成功更新背景图:")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


if __name__ == '__main__':
    unittest.main()