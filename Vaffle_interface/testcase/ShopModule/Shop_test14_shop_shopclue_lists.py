# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------提供店铺线索----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------查询需要提供线索的店铺----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 16
        member_id="b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        print ("testcase_001查询需要提供线索的店铺:")

        result = self.r.interface_requests(member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()