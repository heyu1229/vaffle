#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------关注用户列表----------------------
class Follow_Followers(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------关注我的用户列表----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 3
        print("testcase_001关注我的用户列表：")
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------进入其他用户主页查看关注该用户的列表----------------------------------
    def testcase_002(self):
        sheet_index = 2
        row = 4
        print("testcase_002进入其他用户主页查看关注该用户的列表：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------关注的用户列表为空----------------------------------
    def testcase_003(self):
        sheet_index = 2
        row = 5
        print("testcase_003关注的用户列表为空：")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()