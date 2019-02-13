# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------用户个人中心---------------------------
class MemberCenter(unittest.TestCase):

    def setUp(self):
        self.member_id = '959'
        self.requests = FuncRequests()

    #-----------------查看当前用户信息----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 4
        print("testcase001查看当前用户信息：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()

