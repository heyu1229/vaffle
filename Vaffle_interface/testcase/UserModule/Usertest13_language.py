# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------语言设置-vape_member_extends---语种 1:english  2:russian-----------------------
class Language(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------语言设置english----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 13
        print("testcase001语言设置english：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )
    #
    # #-----------------语言设置russian----------------------------------
    # def testcase_002(self):
    #     sheet_index =0
    #     row = 56
    #     print("testcase002语言设置russian：")
    #     result = self.requests.interface_requests(self.member_id,sheet_index,row)
    #     self.assertEqual ( 10000, result['code'] )
    #     print ( "code返回值：10000" )
    #     self.assertEqual ( '', result['msg'] )
    #     print ( "msg返回值：ok" )
    #
    # # -----------------language 为数字----------------------------------
    # def testcase_003(self):
    #     sheet_index =0
    #     row = 57
    #     print("testcase003 language 为数字：")
    #     result = self.requests.interface_requests(self.member_id,sheet_index,row)
    #     self.assertEqual ( 9999, result['code'] )
    #     print ( "code返回值：9999" )
    #     self.assertEqual ( 'Time out.', result['msg'] )
    #     print ( "msg返回值：Time out." )
    #
    #
    # # -----------------language为特殊字符----------------------------------
    # def testcase_004(self):
    #     sheet_index =0
    #     row = 58
    #     print("testcase004 language为特殊字符：")
    #     result = self.requests.interface_requests(self.member_id,sheet_index,row)
    #     self.assertEqual ( 9999, result['code'] )
    #     print ( "code返回值：9999" )
    #     self.assertEqual ( 'Time out.', result['msg'] )
    #     print ( "msg返回值：Time out." )

if __name__ == '__main__':
    unittest.main()
