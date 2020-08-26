# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------积分流水记录-type:all、add、reduce---------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------积分流水记录-all---------------------------------
    def testcase_001(self):
        sheet_index = 8
        row = 3
        print("testcase001 积分流水记录-all：")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'page':1,'type':'all'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------积分流水记录-add---------------------------------
    def testcase_002(self):
        sheet_index = 8
        row = 4
        print("testcase002 积分流水记录-add：")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'page': 1, 'type': 'add'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


    #-----------------积分流水记录-reduce---------------------------------
    def testcase_003(self):
        sheet_index = 8
        row = 5
        print("testcase003 积分流水记录-reduce：")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'page': 1, 'type': 'reduce'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()