#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests
#---------------用户关注列表----------------------
class Following(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------我关注的用户列表----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 4
        print("testcase_001我关注的用户列表：")
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()