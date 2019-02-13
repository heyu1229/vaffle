# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------消息通知是否开启接收设置  ---------------------------
class Notification(unittest.TestCase):

    def setUp(self):
        self.member_id = '959'
        self.requests = FuncRequests()
    #-----------------消息通知接收全开启----------------------------------
    #-------------vape_member_switch表  1:followers 2:attention 3:like 4:comment 5:sound-  setting 1开启 0关闭-------------
    def testcase_001(self):
        sheet_index =0
        row = 8
        print("testcase001消息通知接收全开启：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )


if __name__ == '__main__':
    unittest.main()
