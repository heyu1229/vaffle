# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

    #---------------邀请回答---------------------
class content(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    def testcase_001(self):

        sheet_index = 1
        row = 92
        print("testcase_001 邀请回答：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload = {'member_uuid':'6dcd1821-1009-4c7d-a718-261ea5f1230c','question_id':98796}

        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()