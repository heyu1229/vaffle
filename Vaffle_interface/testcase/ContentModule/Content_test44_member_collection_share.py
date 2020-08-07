# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------开启取消收藏分享----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------开启收藏分享----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 58
        print("testcase_001 开启收藏分享：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'is_share':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------取消收藏分享----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 59
        print("testcase_002 取消收藏分享：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'is_share':0}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()