# -*- coding:UTF-8 -*-
import unittest
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------产品详情----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------产品详情----------------------------------
    def testcase_001(self):
        sheet_index = 15
        row = 1
        member_uuid='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001品牌型号数据测试:")

        payload = {'goods_id':11}
        result=self.r.interface_requests_payload(member_uuid,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
