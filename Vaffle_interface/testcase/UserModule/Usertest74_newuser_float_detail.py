# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd

from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------新人注册礼-h5详情--------------------
class medal_lists(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()
        self.base_url="https://apitest.vaffle.com/web/newuser/float/detail"

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
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()