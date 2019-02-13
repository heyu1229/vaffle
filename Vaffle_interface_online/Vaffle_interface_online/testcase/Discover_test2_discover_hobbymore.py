# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests


#---------------更多相同设备的用户----------------------
class Discover_hobbymore(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()


    #-----------------更多相同设备的用户----------------------------------

    def testcase_001(self):
        sheet_index =4
        row = 2
        print("testcase001 更多相同设备的用户：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()