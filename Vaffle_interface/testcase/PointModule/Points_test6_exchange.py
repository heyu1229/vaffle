# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------兑换商品------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        self.r = FuncRequests()
    #-----------------兑换商品----------------------------
    def testcase_001(self):
        sheet_index =8
        row = 8

        goods_id = '6'
        s1 = "update vape_goods set total=100, limit_num=1000000, status=1, score=1 where id="+str(goods_id)
        execute_sql1 = self.r.sql_vaffle(s1)

        # 2.调用收获地址接口获取address_id，然后根据address_id得到商品详情
        urlpart = '/member/address'
        payload = {'type':'default'}
        result1 = self.r.interface_requests_data(self.member_id, urlpart, payload)
        address_id = result1['data']['address_id']
        print('address_id=', address_id)

        print("testcase001 兑换商品：")
        payload = {'goods_id': goods_id, 'address_id':address_id}
        result = self.r.interface_requests_payload(self.member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()