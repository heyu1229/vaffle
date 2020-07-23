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
        self.member_id = '744'
        self.requests = FuncRequests()

    #-----------------查看当前用户信息----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 30
        print("testcase001查看当前用户信息：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


    #-----------------查看其他用户信息----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 31
        print("testcase002查看其他用户信息：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------member_id为空----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 32
        print("testcase003 member_id为空：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10040, result["code"])
        print("code返回值：10040")
        print("msg返回值：This user does not exist.")

    #-----------------member_id不存在----------------------------------

    def testcase_004(self):
        sheet_index =0
        row = 33
        print("testcase004 member_id不存在：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10040, result["code"])
        print("code返回值：10040")
        print("msg返回值：This user does not exist.")

if __name__ == '__main__':
    unittest.main()

