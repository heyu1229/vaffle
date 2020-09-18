# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

class Invite_get_score(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------邀请得积分--------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 34
        print("testcase_001 反馈：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {'member_uuid':self.member_uuid}
        result=self.requests.interface_requests_payload(self.member_uuid, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()