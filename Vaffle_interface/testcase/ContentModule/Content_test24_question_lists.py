# -*- coding:UTF-8 -*-
import unittest,time
from Vaffle_interface.public_1.func_requests import FuncRequests


# ---------------Q／A列表---------------------
class CommentsPublish(unittest.TestCase):
    def setUp(self):
        self.r = FuncRequests()

    # -----------------Q／A列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 35
        print("testcase_001 Q／A列表第一页数据：")
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload = {"page":1,"type":"qa",'goods_id':3}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()