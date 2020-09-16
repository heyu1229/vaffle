# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

    #---------------违规记录---------------------
class posts_violation_list(unittest.TestCase):
    def setUp(self):
        self.r = FuncRequests()

    def testcase_001(self):
        sheet_index = 1
        row = 80
        print("testcase_001 违规记录：")
        payload = {"page": 1}
        member_id = "92fe76f8-6b8d-4c5b-9fb1-99f4407afe96"

        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()