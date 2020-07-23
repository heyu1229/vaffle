# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests


#---------------发热门搜索hot searches----------------------
class Discover(unittest.TestCase):

    def setUp(self):
        self.member_id = '745'
        self.requests = FuncRequests()

    #-----------------discover页推荐数据（用户、店铺）----------------------------------
    def testcase_001(self):
        sheet_index =4
        row = 5
        print("testcase001 discover页推荐数据（用户、店铺）：")
        payload = {"lat":"31","lon":"121"}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()
