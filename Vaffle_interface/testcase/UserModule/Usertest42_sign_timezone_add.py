# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------签到 - 添加用户时区【POST】----------------------
class Sign_timezone_add(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------签到 - 添加用户时区【POST】----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 42
        
        print("testcase_001签到 用户时区-14到+14：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # def testcase_002(self):
    #     sheet_index = 0
    #     row = 131
    #
    #     print ( "testcase_001签到 用户时区外：" )
    #     result = self.requests.interface_requests ( self.member_id, sheet_index, row )
    #     self.assertEqual ( 10003, result['code'] )
    #     print ( "code返回值：10003" )

if __name__ == "__main__":
    unittest.main()