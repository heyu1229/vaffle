# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------管理我的店铺 - 功能项----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------管理我的店铺 - 功能项----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 7
        result=self.requests.interface_requests(self.member_uuid,sheet_index,row)

        self.assertEqual(10094, result["code"])

if __name__=="__main__":
    unittest.main()