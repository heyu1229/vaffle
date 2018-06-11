# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------兑换商品详情------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------兑换商品详情----------------------------
    def testcase_001(self):
        sheet_index =8
        row = 10
        # 先调用积分接口获取goods_id，然后根据goods_id得到商品详情
        urlpart = '/membership'
        payload = {}
        result1 = self.requests.interface_requests_data(self.member_id, urlpart, payload)
        goods_id = result1['data']['gifts'][0]['goods_id']

        print("testcase001 兑换商品详情：")
        payload = {'goods_id': goods_id}
        result = self.requests.interface_requests_payload(self.member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()