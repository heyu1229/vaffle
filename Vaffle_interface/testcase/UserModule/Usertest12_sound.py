# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------声音开关  vape_member_switch表---------------------------
class Sound(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------开声音----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 12
        print("testcase001开声音：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )
    # # -----------------sound字段为数字+字母----------------------------------
    # def testcase_002(self):
    #     sheet_index =0
    #     row = 53
    #     print("testcase002 sound字段为数字+字母：")
    #     result = self.requests.interface_requests(self.member_id,sheet_index,row)
    #     self.assertEqual ( 9999, result['code'] )
    #     print ( "code返回值：9999" )
    #     self.assertEqual ( 'Time out.', result['msg'] )
    #     print ( "msg返回值：Time out." )
    #
    # # -----------------sound字段为特殊字符----------------------------------
    # def testcase_003(self):
    #     sheet_index =0
    #     row = 54
    #     print("testcase003 sound字段为特殊字符：")
    #     result = self.requests.interface_requests(self.member_id,sheet_index,row)
    #     self.assertEqual (9999, result['code'] )
    #     print ( "code返回值：9999" )
    #     self.assertEqual ( 'Time out.', result['msg'] )
    #     print ( "msg返回值：Time out." )


if __name__ == '__main__':
    unittest.main()
