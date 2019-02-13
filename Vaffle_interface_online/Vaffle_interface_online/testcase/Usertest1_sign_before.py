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

if __name__ == '__main__':
    unittest.main ()
