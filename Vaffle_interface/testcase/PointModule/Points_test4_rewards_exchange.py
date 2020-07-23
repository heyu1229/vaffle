# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------兑换优惠---------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------兑换优惠积分不足--------------------------------
    def testcase_001(self):
        sheet_index =8
        row = 6
        print("testcase001 兑换优惠积分不足：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10049, result['code'])
        print("code返回值：10049")
        self.assertEqual('The card expires.', result['msg'])
        print("msg返回值：The card expires.")



    # -----------------用户兑换等级不够-------422等级为最低级-------------------------
    def testcase_002(self):
        sheet_index =8
        row = 7
        print("testcase002 用户兑换等级不够：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10049, result['code'])
        print("code返回值：10049")

        self.assertEqual("The card expires.", result['msg'])
        print("msg返回值：The card expires.")

if __name__ == '__main__':
    unittest.main()