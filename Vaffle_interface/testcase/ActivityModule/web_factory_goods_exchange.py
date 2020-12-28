'''
@create : lisa
@file :form_ftk.py
@Date :2020/11/6
@desc :

'''
# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------组装工厂兑换商品---------------------------
class form(unittest.TestCase):

    def setUp(self):
        self.member_uuid = "9db379cd-e4f0-4ad8-bd4e-037541b9985f"
        self.url1="https://apitest.vaffle.com/web/factory/goods/exchange"
    def testcase_001(self):
        headers = {"device": "android ", "version": "4.1.1", "lang": "en", "timestamp": "1493780505",
                   "tik": "UjJGdVNoS2c1VnNRSG9MbkFmVlR2OVdiSHg0S2RCU2dnakFSKzR0OXNnVXFVODdRWDkrT0NYL0dOeU92UURrNVZLTHhBOUFtR1puZ3JhdHNKTVAwanozM2V1ZnJaSUZWTkMwNUlseldhUjZrbmE0dytjY0JWZkduK0psVjN4OVlqdjc0UldOZW83amFqNGR1c2V1WkhyL2JVaUFuUHJOc3l3L0lhTTdacVk4PQ==",
                   }
        payload = {'goodsId': "171",'addressId': '7561'}
        r =  requests.post(self.url1, params=payload, headers=headers)
        result = r.json ()
        print(result)

if __name__ == '__main__':
    unittest.main()