#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------互相关注列表----------------------
class Follow_Followers(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------查看我的朋友----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 5
        print("testcase_001查看我的朋友：")
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        data = result["data"]
        try:
            self.assertEqual([], data["list"])
            print("朋友列表为空")
        except AssertionError as e:
            print("朋友列表不为空")

if __name__=="__main__":
    unittest.main()