# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests
#---------------店铺详情（post部分）----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------店铺详情（post部分）----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 12
        member_id="b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        print ("testcase_001店铺详情（post部分）:")

        result = self.r.interface_requests(member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()