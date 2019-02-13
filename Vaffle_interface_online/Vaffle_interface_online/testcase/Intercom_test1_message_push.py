'''
# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests

#---------------系统消息推送接口---vape_system_notice表-(15服务没有装VPN所以没推送)------------------
class MessagePush(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()

    #-----------------系统消息推送----------------------------------
    def testcase_001(self):
        sheet_index =7
        row = 1
        print("testcase001 系统消息推送：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        try:
            self.assertEqual('send', result['msg'])
            print("msg返回值：send")
        except AssertionError as e:
            print("msg返回报错")
'''
'''
if __name__ == '__main__':
    unittest.main()
'''
