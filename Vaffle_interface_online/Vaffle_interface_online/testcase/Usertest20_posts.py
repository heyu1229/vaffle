# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------用户个人post列表--------vape_posts表 type:2.2.0接口只有all------------
class List(unittest.TestCase):

    def setUp(self):
        self.member_id = '959'
        self.requests = FuncRequests()

    #-----------------用户个人post列表 all----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 15
        print("testcase001 用户个人post列表 all：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()