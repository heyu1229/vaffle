# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------众裁-认证考试题【POST】---------------------
class arbitrate_exam(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    def testcase_001(self):
        sheet_index = 1
        row = 77
        print("testcase_001 认证考试题：")
        payload = {}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()