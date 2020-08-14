# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------新人注册礼领取----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.member_uuid = "da1054cf-bbb6-4df0-a57c-1c654346e208"
        self.requests = FuncRequests ()
        self.base_url="https://apitest.vaffle.com/web/newuser/float/receive"


    # 用户已登录
    def testcase_001(self):
        # 获取token
        payload = {}
        headers = {"device": "android", "version": "4.0.5", "lang": "en", "timestamp": "1564033489234",
                   "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                   "uuid": "64e420ad-571d-4bf3-824d-270c9ba74215",
                   "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "8.0.0","tik":"L3hFbGtnSldjc21Mc0NFcndweFlweEVkaDIwYkNUelBtRXcyc25XSHBqVlBtWWcza2hXR0RpTys4czFxL3VWT2V5ejZjMVlqblI1SW00dTBUTVY4ekhLcTZNOTRjMlRBVkE5Q1N6UEZHNnNZakNpdExBcnJpMmRXb0crSG1paFNUZ01tVnovd3VjYXZadTZVbHNrUmU1UytzK3VuRm1PN3FvTElVYmJpODRjPQ"}
        result = requests.post ( self.base_url, params=payload, headers=headers )
        result = result.json ()
        if result['code']==10000 or result['code']==10301:
            print("testcase pass")
        else:
            self.assertEqual(10000, result['code'])


    # #-------------------非第三方用户不能更新密码--------------------------------
    # def testcase_002(self):
    #     sheet_index = 0
    #     row = 146
    #     print("testcase_002 非第三方用户不能更新密码：")
    #     payload={"normal_member_id":745,"password":"111111","platform":"twitter"}
    #     result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
    #     self.assertEqual(10128, result['code'])
    #     print("code返回值：10128")


if __name__ == "__main__":
    unittest.main()