# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys

from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#---------------钱包 - 删除可提现账户----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.requests=FuncRequests()
       self.member_uuid = '9ccc4119-f04d-43b5-9c0f-c3cf679fe4c9'

    #-----------------钱包 - 删除可提现账户----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 7
        print("testcase_001钱包 - 删除可提现账户：")

        # 调用提现账户添加接口获取account_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        urlpart1 = '/wallet/account/add'
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"account": date, "first_name": "yu", "last_name": "qin"}
        result1 = self.requests.interface_requests_data(self.member_uuid, urlpart1, payload1)
        #list = result1["data"]["account_id"]
        urlpart2='/wallet/account/lists'
        payload2={}
        result2 = self.requests.interface_requests_data(self.member_uuid, urlpart2, payload2)
        #account_uuid = list[0]["account_uuid"]
        account_uuid = result2["data"]["list"][0]["account_uuid"]
        print(account_uuid)
        payload ={"account_uuid":account_uuid}
        result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row,payload)
        # self.assertEqual(10000, result['code'])
        # print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()