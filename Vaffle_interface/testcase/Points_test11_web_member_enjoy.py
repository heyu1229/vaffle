# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------双11活动页------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.member_uuid = "acaf5442-c321-46ee-b3d8-29f563c405c2"
        self.requests = FuncRequests()
    #-----------------双11活动页-返回所有----------------------------
    def testcase_001(self):
        sheet_index =8
        row = 14

        print("testcase001 兑换订单列表-返回所有：")
        result = self.requests.interface_requests(self.member_uuid, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------双11活动页-返回会员尊享----------------------------
    def testcase_002(self):
        sheet_index =8
        row = 15

        print("testcase002 兑换订单列表-返回会员尊享：")
        result = self.requests.interface_requests(self.member_uuid, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()