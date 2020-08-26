# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------禁言、解禁接口----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------禁言--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 35
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 禁言:")

        payload = {'type':'ban','member_uuid':'1010827e-e8aa-4d49-ac46-a451b2727a2c','ban_day':3,'guid':'48afaa46-0d80-4518-a880-3577530440d0'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------解禁--------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 36
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_002 解禁:")

        payload = {'type':'unban','member_uuid':'1010827e-e8aa-4d49-ac46-a451b2727a2c','guid':'48afaa46-0d80-4518-a880-3577530440d0'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()