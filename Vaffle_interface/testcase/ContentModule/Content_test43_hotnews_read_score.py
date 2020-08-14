# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------阅读完毕后加积分----------------------
class hotnews_read_score(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------阅读完毕后加积分----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 57
        print("testcase_001 阅读完毕后加积分：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'id':89207}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()