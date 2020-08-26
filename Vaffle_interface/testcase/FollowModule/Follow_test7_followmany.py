#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests
#---------------注册批量关注用户----------------------
class Follow_tips(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------注册批量关注用户----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 8
        print("testcase_001注册批量关注用户：")
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        obj = ('e51ae55c-6131-4d20-a31e-6595a932c84b','f5313da3-4f19-4343-9fa1-fa56d754c280')
        followed_id_arr = json.dumps(obj)
        print('followed_id_arr=',followed_id_arr)
        payload = {"followed_id_arr":followed_id_arr,'follow_state':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()