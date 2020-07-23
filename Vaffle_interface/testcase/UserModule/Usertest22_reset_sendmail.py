# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc

import time,sys

import xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------用户重置密码验证码发送邮件---------------------------
class ResetSendmail(unittest.TestCase):

    def setUp(self):
        self.email = '1929995@omv.com'
        self.member_id = '744'
        self.requests = FuncRequests()

    #-----------------用户重置密码发送验证码----------------------------------
    def testcase_001(self):
        # -----------------先获取验证码---------------------------------
        # 获取路径
        urlpart = "/member/reset_send_mail"
        payload = {"email": self.email}
        sheet_index =0
        row = 79
        result = self.requests.interface_requests_data(self.member_id,urlpart,payload)
        identifycode = result['data']['code']
    # -----------------用户重置密码成功-22：resetpass接口---------------------------------
        password =time.strftime ( "%Y%m%d_%H_%M_%S" )
        payload = {"email": "1929995@omv.com","password":password,"code": identifycode}
        sheet_index =0
        row = 80
        print("testcase001 用户重置密码成功：")
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)

        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：Reset password successfully" )



    #-----------------账户不存在----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 81
        print("testcase002 账户不存在：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10004, result['code'])
        print("code返回值：10004")

        self.assertEqual("The mailbox or username has not been registered, so please sign up.", result['msg'])
        print("msg返回值：The mailbox or username has not been registered, so please sign up.")

    #-----------------非法账户----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 82
        print("testcase003 非法账户：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual(9999, result['code'])
        print("code返回值：9999")

        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

        gc.collect()
if __name__ == '__main__':
    unittest.main()




