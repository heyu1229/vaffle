# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------首页动态列表4.0.7-----------------
class home_recommend(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------首页动态列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 67
        print("testcase_001 首页动态列表：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'type':'following','page':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()