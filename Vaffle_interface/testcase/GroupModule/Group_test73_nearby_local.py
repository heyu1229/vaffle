# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#------------------local----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #----------------------local------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 85
        print("testcase_001 local:")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'page':1}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()