# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc

import time
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------修改用户邮箱----------------------
class ChangeEmail(unittest.TestCase):

    def setUp(self):
        self.member_id = '760'
        self.requests = FuncRequests()
    #-----------------修改用户邮箱成功----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 40
        print("testcase001 修改用户邮箱成功：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    #-----------------修改为已存在的用户邮箱----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 41
        print("testcase002 修改为已存在的用户邮箱：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10002, result['code'])
        print("code返回值：10002")
        self.assertEqual('The email address has been taken.', result['msg'])
        print("msg返回值：The email address has been taken.")


    #-----------------修改的邮箱格式不正确----------------------------------

    def testcase_003(self):
        sheet_index =0
        row = 42
        print("testcase003 修改的邮箱格式不正确：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result['code'])
        print("code返回值：9999")

        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")


if __name__ == '__main__':
    unittest.main()