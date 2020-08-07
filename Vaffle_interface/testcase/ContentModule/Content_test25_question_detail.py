# -*- coding:UTF-8 -*-
import unittest,time
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------单条QA的详情---------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------单条QA的详情----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 36
        print("testcase_001 单条QA的详情：")

        question_id="19183"
        payload = {"question_id": question_id}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()