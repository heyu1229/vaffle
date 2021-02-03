# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests



#---------------热门搜索hot searches----------------------
class search(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    def testcase_001(self):

        sheet_index = 9
        row = 1
        print("testcase001 热门搜索hot searche：")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {"type":"goods"}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()