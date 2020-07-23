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
        row = 12
        print("testcase001 用户注册成功:")
        nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        nickname = 'heyu'+nowTime
        email = 'heyu'+nowTime+'@qq.com'
        print(email)
        payload = {'email': email,'password': 'aaa111','displayname': 'heyu','nickname': nickname,'equipment_number': 'PE-TL10',}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


    #-----------------nickname已存在----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 13
        print("testcase002 nickname已存在：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10044, result["code"])
        print("code返回值：10044")
        self.assertEqual('This username is occupied. Please try another one.', result['msg'])
        print("msg返回值：This username is occupied. Please try another one.")

    # -----------------nickname为空----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 14
        print("testcase003 nickname为空：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result["code"])
        print("code返回值：9999")
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------nickname少于3位----------------------------------
    def testcase_004(self):
        sheet_index =0
        row = 15
        print("testcase004 nickname少于3位：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The username should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The username should be 3-30 characters (letters, digits or underline)" )

    # -----------------nickname超过30位----------------------------------
    def testcase_005(self):
        sheet_index =0
        row = 16
        print("testcase005 nickname超过30位：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The username should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The username should be 3-30 characters (letters, digits or underline)" )

    # -----------------nickname字符前有空格报错----------------------------------
    def testcase_006(self):
        sheet_index =0
        row = 17
        print("testcase006 nickname字符前有空格报错：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The username should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The username should be 3-30 characters (letters, digits or underline)" )

    # -----------------nickname字符间有空格报错----------------------------------
    def testcase_007(self):
        sheet_index =0
        row = 18
        print("testcase007 nickname字符间有空格报错：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The username should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The username should be 3-30 characters (letters, digits or underline)" )

    # -----------------nickname含特殊字符报错----------------------------------
    def testcase_008(self):
        sheet_index =0
        row = 19
        print("testcase008 nickname含特殊字符报错：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The username should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The username should be 3-30 characters (letters, digits or underline)" )

    # -----------------邮箱账号已被注册----------------------------------
    def testcase_009(self):
        sheet_index =0
        row = 20
        print("testcase009 nickname含特殊字符报错：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10002, result['code'] )
        print ( "code返回值：10002" )

        self.assertEqual ( 'The email address has been taken.', result['msg'] )
        print ( "msg返回值：The email address has been taken." )

    # -----------------邮箱账号格式错误----------------------------------
    def testcase_010(self):
        sheet_index =0
        row = 21
        print("testcase010 邮箱账号格式错误：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual ( 10058, result['code'] )
        print ( "code返回值：10058" )
        self.assertEqual ( 'Mailbox Error', result['msg'] )
        print ( "msg返回值：Mailbox Error" )

    # -----------------密码不足6位----------------------------------
    def testcase_011(self):
        sheet_index =0
        row = 22
        print("testcase011 密码不足6位：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )

        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------密码超过20位----------------------------------
    def testcase_012(self):
        sheet_index =0
        row = 23
        print("testcase012 密码超过20位：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------密码不限特殊字符----------------------------------
    def testcase_013(self):
        sheet_index =0
        row = 24
        print("testcase001 用户注册成功:")
        nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        nickname = 'heyu'+nowTime
        email = 'heyu'+nowTime+'@qq.com'
        print(email)
        payload = {'email': email, 'password': 'aaa$$111', 'displayname': 'heyu', 'nickname': nickname,'equipment_number': 'PE-TL10', }
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == '__main__':
    unittest.main ()









