# -*- coding:UTF-8 -*-
import unittest,time
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------用户关注的 Q／A 列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------用户关注的 Q／A 列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 40
        print("testcase_001 用户关注的 Q／A 列表：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload = {"page": 1,"type": "qa","member_id":member_id}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()