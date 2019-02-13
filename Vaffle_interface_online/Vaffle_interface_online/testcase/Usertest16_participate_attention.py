# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------用户被@的数据集合列表----vape_attention表type: 1 post 2 comment------------------
class ParticipateAttention(unittest.TestCase):

    def setUp(self):
        self.member_id = '959'
        self.requests = FuncRequests()
    #-----------------用户被@的数据post ----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 13
        print("testcase001 用户被@的数据post：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


if __name__ == '__main__':
    unittest.main()