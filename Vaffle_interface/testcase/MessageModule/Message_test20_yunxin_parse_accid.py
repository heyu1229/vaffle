# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------accid更新云信ex信息---------------------
class Message(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------accid更新云信ex信息---------------------------------
    def testcase_001(self):
        sheet_index = 5
        row = 21
        print("testcase_001 accid更新云信ex信息：")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'accid':'test_960'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()