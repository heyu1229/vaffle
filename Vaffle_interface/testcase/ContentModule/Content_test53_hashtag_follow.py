# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests



#--------------【HashTag】-关注/取消关注---------------------
class hashtag_follow(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------【HashTag】-关注hashtag----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 72
        print("testcase_001 【HashTag】关注hashtag：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {"tag_id":116183,"status":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------【HashTag】-取消关注hashtag----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 73
        print("testcase_002 【HashTag】取消关注hashtag：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {"tag_id":116183,"status":0}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()