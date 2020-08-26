# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------搜索群内成员----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------搜索群内成员---------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 7
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print("testcase_001 搜索群内成员:")

        payload = {"page": "1","guid": "48afaa46-0d80-4518-a880-3577530440d0","search_name": "lisa","type":"normal"}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()