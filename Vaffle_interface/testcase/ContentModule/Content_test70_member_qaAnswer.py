# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

    #---------------用户个人qa-answer列表---------------------
class content(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    def testcase_001(self):

        sheet_index = 1
        row = 90
        print("testcase_001 用户个人qa-answer列表：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload = {'type':'all','page':1,'member_uuid':'348a307e-a57d-4813-ade9-bff94aa10601'}


        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()