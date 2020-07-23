# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------用户喜欢的post列表----------------------
class List(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------用户喜欢的post列表 all---vape_post_praise表-------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 75
        print("testcase001 用户喜欢的post列表：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


    # -----------------用户喜欢的post列表 photo----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 76
        print("testcase002 用户喜欢的post列表 photo：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

    # -----------------用户喜欢的post列表 video----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 77
        print("testcase003 用户喜欢的post列表 video：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

if __name__ == '__main__':
    unittest.main()