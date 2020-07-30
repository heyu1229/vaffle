# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc
import time,sys
import xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------用户重置密码验证码发送邮件---------------------------
class ResetSendmail(unittest.TestCase):

    def setUp(self):
        self.email = '1004856404@qq.com'
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()

    #-----------------用户重置密码发送验证码----------------------------------
    def testcase_001(self):
        # -----------------先获取验证码---------------------------------
        # 获取路径
        sheet_index =0
        row = 21
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
    #     identifycode = result['data']['code']
    # # -----------------用户重置密码成功-22：resetpass接口---------------------------------
    #     password =time.strftime ( "%Y%m%d_%H_%M_%S" )
    #     payload = {"email": "1004856404@qq.com","password":password,"code": identifycode}
    #     sheet_index =0
    #     row = 21
    #     print("testcase001 用户重置密码成功：")
    #     result = self.requests.interface_requests_payload(self.member_uuid,sheet_index,row,payload)

        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )

if __name__ == '__main__':
    unittest.main()




