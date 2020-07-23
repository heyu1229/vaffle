# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------用户个人信息---------------------------
class MemberInfo(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------查看存在的当前用户信息，is_verify邮箱是否已经验证 1:是 0:否----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 34
        print("testcase001查看当前用户信息：")
        payload={"member_id":744}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()
