# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------扫码登录结果（H5轮询调用检测授权结果）-----------------------
class qrcode_oauth_login(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    def testcase_001(self):
        sheet_index = 3
        row = 40
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        result=self.requests.interface_requests(self.member_uuid, sheet_index, row)
        if result["code"]==10000:
            print("pass")
        elif result["code"]==10325:
            print("pass")
        else:
            print("fail")
            self.assertEqual(10000, result["code"])

if __name__ == '__main__':
    unittest.main()