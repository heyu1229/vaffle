# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc

import time
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------用户参与的comment----------------------
class ParticipateComments(unittest.TestCase):

    def setUp(self):
        self.member_id = '980'
        self.requests = FuncRequests()
    #-----------------评论列表有多个--to -vape_post_comments表 post_publisher 为744---------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 60
        print("testcase001 评论列表有多个to：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")



    #-----------------评论列表有多个--from----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 61
        print("testcase002 评论列表有多个from：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()