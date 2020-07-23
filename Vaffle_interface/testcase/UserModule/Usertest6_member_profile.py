# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------修改用户资料---------------------------
class MemberProfile(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()

    #-----------------修改用户资料,gender:用户性别 M:男 F:女 N:保密----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 35
        print("testcase001修改用户资料：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()