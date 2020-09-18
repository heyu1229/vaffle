# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------注册抽奖和新客福利抽奖弹窗-----------------------
class System_baseornew(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    def testcase_001(self):
        sheet_index = 3
        row = 36
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        result=self.requests.interface_requests(self.member_uuid, sheet_index, row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()