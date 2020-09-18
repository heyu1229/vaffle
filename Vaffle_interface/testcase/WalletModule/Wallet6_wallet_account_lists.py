# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys

#------------------------钱包 - 提现记录---------------------------
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url


class wallet_income(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()

    def testcase_001(self):
        sheet_index =13
        row = 6
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")



    #-----------------钱包 - 提现账户申请----------------------------------
    # def testcase_001(self):
    #
    #     s = "delete from vape_reflect_record where member_id='70493'"
    #     execute_sql = self.requests.sql_vaffle(s)
    #     s1="update vape_wallet set balance=100,frozen_money=0 where member_id='70493'"
    #     execute_sql1 = self.requests.sql_vaffle(s1)
    #     #1.因为提现最小金额是50，所以要先去数据库将balane改成比frozen_money大50才能执行该用例
    #     #2.因为一个月只能提现一次，所以要先删除数据库中表vape_reflect_record中该用户的当月提现记录
    #     sheet_index = 1
    #     row = 6
    #     print("testcase_001钱包 - 发起提现申请：")
    #
    #     date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     payload = {"account":date,"money":"50"}
    #     result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row, payload)
    #     self.assertEqual(10000, result['code'])
    #     print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()