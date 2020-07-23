# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------用户重置密码---------------------------
class ResetPass(unittest.TestCase):

    def setUp(self):
        self.member_id = '452'
        self.email = '1929996@omv.com'
        self.requests = FuncRequests()

    # -----------------新密码与旧密码一致----------------------------------
    def testcase_001(self):
        # -----------------先获取验证码---------------------------------
        # 获取路径
        urlpart = "/member/reset_send_mail"
        payload = {"email": "1929996@omv.com"}
        result = self.requests.interface_requests_data ( self.member_id, urlpart, payload )
        identifycode = result['data']['code']

        payload = {"email": "1929996@omv.com", "password": "123456", "code": identifycode}
        sheet_index =0
        row = 83
        print("testcase001 新密码与旧密码一致：")
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)

        self.assertEqual(10032, result['code'])
        print("code返回值：10032")
        self.assertEqual('The password is the same as the old one, so please input another one.', result['msg'])
        print("msg返回值：The password is the same as the old one, so please input another one.")


    # -----------------验证码超长----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 84
        print("testcase002 验证码超长：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.',result['msg'])
        print("msg返回值：Time out.")


    # -----------------验证码为空----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 85
        print("testcase003 验证码为空：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.',result['msg'])
        print("msg返回值：Time out.")

    #-----------------账户不存在----------------------------------

    def testcase_004(self):
        sheet_index =0
        row = 86
        print("testcase004 账户不存在：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10004, result['code'])
        print("code返回值：10004")
        self.assertEqual("The mailbox or username has not been registered, so please sign up.", result['msg'])
        print("msg返回值：The mailbox or username has not been registered, so please sign up.")
    # -----------------验证码错误----------------------------------
    def testcase_005(self):
        sheet_index =0
        row = 87
        print("testcase005 验证码错误：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10009, result['code'])
        print("code返回值：10009")
        self.assertEqual('Verification Code Error',result['msg'])
        print("msg返回值：Verification Code Error")

if __name__ == '__main__':
    unittest.main()





