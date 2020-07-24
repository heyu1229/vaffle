# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import time
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#------------------------被其他用户点赞的post列表---------------------------
class ParticipateLikes(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------被其他用户点赞的post列表----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 14
        print("testcase001 被其他用户点赞的post列表：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

if __name__ == '__main__':
    unittest.main()
