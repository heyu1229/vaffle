# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#---------------获取商业级用户的登录信息----------------------
class Brands(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------获取商业级用户的登录信息----------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 36
        print("testcase_001获取商业级用户的登录信息：")
        payload = {"normal_member_uuid":"a5f10151-5685-4432-8c35-7198bc6511c9",
                   "target_role_uuid":"cafe166a-8842-457e-8467-82f18d00275d","fcm_token":"fcm_token"}
        result = self.requests.interface_requests_payload(self.member_uuid, sheet_index, row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()