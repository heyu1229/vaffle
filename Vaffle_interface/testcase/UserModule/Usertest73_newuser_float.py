# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd

from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------新人注册礼-弹窗--------------------
class medal_lists(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()


    def testcase_001(self):
        sheet_index = 0
        row = 73
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        if result['code']==10000 or result['code']==10305:
            print("testcase pass")
        else:
            self.assertEqual(10000, result['code'])



if __name__ == "__main__":
    unittest.main()