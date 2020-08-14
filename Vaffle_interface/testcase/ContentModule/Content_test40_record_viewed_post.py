# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------记录被浏览的帖子----------------------
class record_viewed_post(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------记录被浏览的帖子----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 54
        print("testcase_001 记录被浏览的帖子：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        obj = ({"member_id":member_id, "post_ids":(46,55,56,67)},)
        p = json.dumps(obj)
        payload = {"p":p}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()