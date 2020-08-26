# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------兑换结果回执------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        self.r = FuncRequests()
    #-----------------兑换结果回执----------------------------
    def testcase_001(self):
        sheet_index =8
        row = 10

        print("testcase001 兑换结果回执：")
        payload = {'goods_id': 6}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10152, result['code'])
            print("code返回值：10152")

if __name__ == '__main__':
    unittest.main()