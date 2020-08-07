# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests



#--------------【HashTag】-人气 / 最新 列表---------------------
class hashtag_post_lists(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------【HashTag】-人气列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 70
        print("testcase_001 【HashTag】人气列表：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {"tag_name":"zzzzz","type":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------【HashTag】-最新列表----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 71
        print("testcase_002 【HashTag】最新列表：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {"tag_name":"zzzzz","type":2}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()