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
        row = 3
        print("testcase001 用邮箱登录成功：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()
    











