#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests
#---------------获取粉丝人数----------------------
class Follow_tips(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------获取粉丝人数----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 7
        print("testcase_001获取粉丝人数：")
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload = {"target_role":'b9f73f23-7bc6-4de6-9f9b-df2c98076221'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()