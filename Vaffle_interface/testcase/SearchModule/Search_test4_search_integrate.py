# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------综合搜索功能----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    # -----------------搜索post数据----------------------------------
    def testcase_001(self):
        sheet_index = 9
        row = 4
        print("testcase_001搜索post数据：")
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'type': 'post','keywords':'queen','page':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------搜索news数据----------------------------------
    def testcase_002(self):
        sheet_index = 9
        row = 5
        print("testcase_002搜索news数据：")
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'type': 'news','keywords':'queen','page':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------搜索qa数据----------------------------------
    def testcase_003(self):
        sheet_index = 9
        row = 6
        print("testcase_003搜索qa数据：")
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'type': 'qa','keywords':'queen','page':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
