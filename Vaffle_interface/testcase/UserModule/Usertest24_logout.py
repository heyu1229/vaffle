# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------用户退出接口---------------------------
class Logout(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------用户退出----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 88
        print("testcase001 用户退出登录：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('logout success', result['msg'])
        print("msg返回值：logout success")

    gc.collect ()
if __name__ == '__main__':
    unittest.main()