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
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------消息通知接收全开启----------------------------------
    #-------------vape_member_switch表  1:followers 2:attention 3:like 4:comment 5:sound-  setting 1开启 0关闭-------------
    def testcase_001(self):
        sheet_index =0
        row = 46
        print("testcase001消息通知接收全开启：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

    # -----------------消息通知接收全关闭----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 47
        print("testcase002 消息通知接收全关闭：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

    # -----------------消息通知followers字段为数字----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 48
        print("testcase003 消息通知followers字段为数字：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )


    # -----------------消息通知attention字段为数字+字母----------------------------------
    def testcase_004(self):
        sheet_index =0
        row = 49
        print("testcase004 消息通知attention字段为数字+字母：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------消息通知like字段为aaa----------------------------------
    def testcase_005(self):
        sheet_index =0
        row = 50
        print("testcase005 消息通知like字段为aaa：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------消息通知comment字段为特殊字符----------------------------------
    def testcase_006(self):
        sheet_index =0
        row = 51
        print("testcase006 消息通知comment字段为特殊字符：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

if __name__ == '__main__':
    unittest.main()
