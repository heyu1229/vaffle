# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------话题提示功能----------------------
class search(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------获取默认推荐话题----------------------------------
    def testcase_001(self):
        sheet_index = 9
        row = 2
        print("testcase_001获取默认推荐话题：")
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'at_default':'on'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
