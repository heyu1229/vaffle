# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#-----------------------用户登录接口---------------------------
class SignIn(unittest.TestCase):

    def setUp(self):
        self.member_id = 'none'
        self.requests = FuncRequests()


    #-----------------用邮箱登录成功--------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 25
        print("testcase001 用邮箱登录成功：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    # -----------------用nickname登录成功--------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 26
        print("testcase002 用nickname登录成功：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    # -----------------account为空----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 27
        print("testcase003 account为空：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )

        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------输入的邮箱账号不存在----------------------------------
    def testcase_004(self):
        sheet_index =0
        row = 28
        print("testcase004 输入的邮箱账号不存在：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10004, result['code'] )
        print ( "code返回值：10004" )

        self.assertEqual ( "The mailbox or username has not been registered, so please sign up.", result['msg'] )
        print ( "msg返回值：The mailbox or username has not been registered, so please sign up." )

    # -----------------密码不正确----------------------------------
    def testcase_005(self):
        sheet_index =0
        row = 29
        print("testcase005 密码不正确：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10055, result['code'] )
        print ( "code返回值：10055" )

        self.assertEqual ( 'Password Error', result['msg'] )
        print ( "msg返回值：Password Error" )

if __name__ == '__main__':
    unittest.main()
    











