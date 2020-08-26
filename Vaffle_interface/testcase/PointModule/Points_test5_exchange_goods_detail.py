# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------兑换商品详情------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()
    #-----------------兑换商品详情----------------------------
    def testcase_001(self):
        sheet_index =8
        row = 7
        # 先调用积分接口获取goods_id，然后根据goods_id得到商品详情
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        urlpart = '/membership'
        payload = {}
        result1 = self.r.interface_requests_data(member_id, urlpart, payload)
        goods_id = result1['data']['gifts'][0]['goods_id']
        print('goods_id=',goods_id)

        print("testcase001 兑换商品详情：")
        payload = {'goods_id': goods_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()