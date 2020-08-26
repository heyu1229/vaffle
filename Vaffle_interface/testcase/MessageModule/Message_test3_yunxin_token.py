# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------与用户相关的QA信息列表----------------------
class Message(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------获取云信token信息----------------------------------
    def testcase_001(self):
        sheet_index = 5
        row = 3
        print("testcase_001获取云信token信息：")
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()