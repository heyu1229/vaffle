# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------拉黑----------------------
class Member_block(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------拉黑----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 41
        print("testcase_001拉黑：")
        payload = {"member_uuid":"0c6fd624-5b6f-47d2-a91b-e17e992bf056"}
        result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row,payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10112, result['code'])
            print("code返回值：10112")
    #
    # #-----------------不能拉黑自己----------------------------------
    # def testcase_002(self):
    #     sheet_index = 0
    #     row = 122
    #     print("testcase_002不能拉黑自己：")
    #     payload = {"member_id":self.member_id}
    #     result = self.r.interface_requests_payload(self.member_id, sheet_index, row,payload)
    #     self.assertEqual(10003, result['code'])
    #     print("code返回值：10003")
    #

if __name__ == "__main__":
    unittest.main()