# -*- coding:UTF-8 -*-
import unittest,time
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------QA回答的评论列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------QA回答的评论列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 38
        print("testcase_002 用户对于Q／A的回答列表数据：")
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload = {"answer_id": 27261, "page": 1,}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()