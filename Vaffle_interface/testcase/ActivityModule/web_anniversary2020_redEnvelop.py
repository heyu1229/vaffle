'''
@create : lisa
@file :web_anniversary2020_redEnvelop.py
@Date :2020/11/6
@desc :

'''
# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------红包雨play---------------------------
class redEnvelop(unittest.TestCase):

    def setUp(self):
        self.member_uuid = "9db379cd-e4f0-4ad8-bd4e-037541b9985f"
        self.url1="https://api.vaffle.com/web/anniversary2020/redEnvelop"
    #-----------------用户退出----------------------------------
    def testcase_001(self):
        headers = {"device": "android ", "version": "4.1.0", "lang": "en", "timestamp": "1493780505", "tik": "aWtyc2Y0Z1F4NnZKNkdoeDE3R3gzSFdOaUJiU2x3ZHJxU3hoRHQxVU9ZcDZxTEt6R21MWHF5SVZHYWxSRWFEUmpFUjNMU0lXR1NOOU8rK05IeXJsUjM2QmU0Q2V5UUszZzY3L0VTNERKU3JqMTd2UEczU0FqWTRSUkhKS1dRZWg4N0NaOGxOUFV6eVZucHc3b2hWRlF6UzhSbW9PRWE0Zk5NZXJzM2JySkxRPQ==",
                   }
        payload = {'point': "300",'ftk': '1604634172776','type': "1"}
        r =  requests.post(self.url1, params=payload, headers=headers)
        result = r.json ()
        print(result)

if __name__ == '__main__':
    unittest.main()