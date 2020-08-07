# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests



#--------------签到通知当日展示状态---------------------
class sign_signtips_switch(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------签到通知当日展示状态----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 75
        print("testcase_001 签到通知当日展示状态：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == '__main__':
    unittest.main()