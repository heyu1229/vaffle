# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc

import time
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------发送验证link至邮箱  vape_verifyemail_log表---------------------------
class VerifyCode(unittest.TestCase):

    def setUp(self):
        self.member_id = '760'
        self.requests = FuncRequests()
    #-----------------发送验证link至邮箱----------------------------------

    def testcase_001(self):
        sheet_index =0
        row = 43
        print("testcase001发送验证link至邮箱：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

    # -----------------邮箱格式不正确----------------------------------

    def testcase_002(self):
        sheet_index =0
        row = 44
        print("testcase002邮箱格式不正确：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10003, result['code'] )
        print ( "code返回值：10003" )
        self.assertEqual ( 'Parameter Error', result['msg'] )
        print ( "msg返回值：Parameter Error." )


if __name__ == '__main__':
    unittest.main()