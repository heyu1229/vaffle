# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------hashtag搜索----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    # -----------------hashtag搜索----------------------------------
    def testcase_001(self):
        sheet_index = 9
        row = 8
        print("testcase_001 hashtag搜索：")
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'keywords':'queen'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
