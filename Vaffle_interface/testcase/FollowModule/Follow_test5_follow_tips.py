#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------粉丝关注提醒列表----------------------
class Follow_tips(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------粉丝关注提醒列表----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 6
        print("testcase_001粉丝关注提醒列表：")
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        data=result["data"]
        try:
            self.assertEqual([], data["list"])
            print("粉丝关注提醒为空")
        except AssertionError as e:
            print("粉丝关注提醒不为空")

if __name__=="__main__":
    unittest.main()