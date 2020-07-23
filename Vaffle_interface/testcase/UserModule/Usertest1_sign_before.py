# -*- coding:UTF-8 -*-
import json
import unittest
import sys
import global_list
sys.path.append(global_list.path+"/public_1")

from func_requests import FuncRequests
#---------------用户注册第一阶段返回nickname----------------------

class SignBefore(unittest.TestCase):


    def setUp(self):
        self.member_id = 'none'
        self.requests = FuncRequests()

    #-----------------用户注册成功，list返回5个nickname----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 1
        print("testcase001 用户注册成功，list返回5个nickname：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------邮箱账号已被注册----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 2
        print("testcase002 邮箱账号已被注册：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10002, result["code"])
        print("code返回值：10002")
        print("msg返回值：The email address has been taken.")


    #-----------------邮箱账号格式错误----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 3
        print("testcase003 邮箱账号格式错误：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10058, result["code"])
        print("code返回值：10058")
        print("msg返回值：Mailbox Error")

    #-----------------密码不足6位----------------------------------
    def testcase_004(self):
        sheet_index =0
        row = 4
        print("testcase004 密码不足6位：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result["code"])
        print("code返回值：9999")
        print("msg返回值：Time out.")

    #-----------------密码超过20位----------------------------------
    def testcase_005(self):
        sheet_index =0
        row = 5
        print("testcase005 密码超过20位：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result["code"])
        print("code返回值：9999")
        print("msg返回值：Time out.")

    #-----------------密码纯数字----------------------------------
    def testcase_006(self):
        sheet_index =0
        row = 6
        print("testcase006 密码纯数字：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])

    #-----------------密码纯字母----------------------------------
    def testcase_007(self):
        sheet_index =0
        row = 7
        print("testcase007 密码纯字母：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])


    #----------------displayname为空----------------------------------
    def testcase_008(self):
        sheet_index =0
        row = 8
        print("testcase008 displayname为空：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result["code"])
        print("code返回值：9999")
        print("msg返回值：Time out.")


    #-----------------displayname少于3位----------------------------------
    def testcase_009(self):
        sheet_index =0
        row = 9
        print("testcase009 displayname少于3位：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result["code"])
        print("code返回值：9999")
        print("msg返回值：Time out.")

    #-----------------displayname超过30位----------------------------------
    def testcase_010(self):
        sheet_index =0
        row = 10
        print("testcase010 displayname超过30位：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result["code"])
        print("code返回值：9999")
        print("msg返回值：Time out.")

    # -----------------displayname含特殊字符校验通过----------------------------------
    def testcase_011(self):
        sheet_index =0
        row = 11
        print("testcase011 displayname含特殊字符校验通过：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])

if __name__ == '__main__':
    unittest.main ()
