# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------综合搜索----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    # -----------------综合搜索----------------------------------
    def testcase_001(self):
        sheet_index = 9
        row = 11
        print("testcase_001 综合搜索：")

        member_id = '85ed3766-7b44-4bf5-a736-bd397de4eed7'
        payload = {'keywords':'queen','page':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
