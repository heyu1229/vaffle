# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------会员尊享-查看更多------------------
class RewardsDescription(unittest.TestCase):

    def setUp(self):
        self.member_uuid = "acaf5442-c321-46ee-b3d8-29f563c405c2"
        self.requests = FuncRequests()
    #-----------------会员尊享-查看更多----------------------------
    def testcase_001(self):
        sheet_index =8
        row = 13

        # 1.调用登录接口获取tik
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"account": "queen301", "password": "111111" }
        urlpart1 = '/sign/in'
        result1 = self.requests.interface_requests_data(self.member_uuid, urlpart1, payload1)
        tik = result1["data"]["tik"]

        print("testcase001 会员尊享-查看更多：")
        payload={}
        result = self.requests.interface_requests_payload_tik(self.member_uuid, sheet_index, row,payload,tik)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()