# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------申请成为店长 - 申请提交检测----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------申请成为店长 - 申请提交检测----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 30
        member_id = '4e802cdb-5bf2-44b1-90e4-791dacac93f4'
        print ("testcase_001申请成为店长 - 申请提交检测:")

        result = self.r.interface_requests(member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()