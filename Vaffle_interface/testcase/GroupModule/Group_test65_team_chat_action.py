# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#------------------【群聊】- 数据统一交换接口----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #----------------------【群聊】- 数据统一交换接口-------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 76
        print("testcase_001 【群聊】- 数据统一交换接口:")

        params = {"accid":"","announcement":"hhaa","joinmode":"","magree":"0","msg":"","owner":"beta_960",
               "tid":"2876181636"}
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'action':'update','params':params}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()