# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

    #---------------【newTag】 搜索单个---------------------
class newtag_searchall(unittest.TestCase):
    def setUp(self):
        self.r = FuncRequests()

    def testcase_001(self):
        sheet_index = 1
        row = 106
        print("testcase_001 【newTag】搜索单个：")
        payload = {"category": 3,"page":1,"title":"a","last_id":""}
        member_id = "e1399798-f1df-4f22-aea0-da0036ee03f1"

        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()