# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------产品 - 产品列表----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------产品 - 产品列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 31
        member_id='4e802cdb-5bf2-44b1-90e4-791dacac93f4'
        print ("testcase_001产品列表第一页数据:")

        payload={"shop_id":54273}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()