# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc
import time,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------邮箱验证码校验----------------------
class Codecheck(unittest.TestCase):

    def setUp(self):
        self.member_id = '452'
        self.email = '1929996@omv.com'
        self.requests = FuncRequests()
    #-----------------邮箱验证码校验正确forgot----------------------------------
    def testcase_001(self):

        # -----------------先获取验证码---------------------------------
        # 获取路径
        urlpart = "/member/reset_send_mail"
        payload = {"email": self.email}
        sheet_index =0
        row = 79
        result = self.requests.interface_requests_data(self.member_id,urlpart,payload)
        identifycode = result['data']['code']

        print("testcase001 邮箱验证码校验正确forgot：")
        payload = {'email': self.email,'code': identifycode,'type': 'forgot'}
        sheet_index =0
        row = 90
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")



    #-----------------邮箱验证码校验失败----------------------------------
    def testcase_002(self):
        print("testcase002 邮箱验证码校验失败：")
        payload = {"email":"1929995@omv.com","code": "111111","type": "forgot"}
        sheet_index =0
        row = 92
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10009, result['code'])
        print("code返回值：10009")
        self.assertEqual('Verification Code Error', result['msg'])
        print("msg返回值：Verification Code Error")


if __name__ == '__main__':
    unittest.main()