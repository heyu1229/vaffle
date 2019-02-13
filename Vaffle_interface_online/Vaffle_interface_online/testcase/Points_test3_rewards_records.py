# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------积分流水记录-type:all、add、reduce---------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------积分流水记录-all---------------------------------
    def testcase_001(self):
        sheet_index =8
        row = 3
        print("testcase001 积分流水记录-all：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


    #-----------------积分流水记录-add---------------------------------
    def testcase_002(self):
        sheet_index =8
        row = 4
        print("testcase002 积分流水记录-add：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


    #-----------------积分流水记录-reduce---------------------------------
    def testcase_003(self):
        sheet_index =8
        row = 5
        print("testcase003 积分流水记录-reduce：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()