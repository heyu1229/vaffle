# -*- coding:UTF-8 -*-
import json
import unittest
import requests,gc
import sys

import time
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#-----------------------用户注册最后阶段接口---------------------------
class SignUp(unittest.TestCase):

    def setUp(self):
        self.member_id = 'none'
        self.requests = FuncRequests()

    #-----------------注册成功----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 2
        print("testcase001 用户注册成功:")
        nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        nickname = 'heyu'+nowTime
        email = 'heyu'+nowTime+'@qq.com'
        print(email)
        payload = {'email': email,'password': 'aaa111','displayname': 'heyu','nickname': nickname,'equipment_number': 'PE-TL10',}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == '__main__':
    unittest.main ()









