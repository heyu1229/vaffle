# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------检测用户是否设置 （第三方） 登录密码----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-------------------非第三方平台账户--------------------------------
    def testcase_001(self):
        sheet_index = 0
        row = 50
        print("testcase_001 非第三方平台账户：")
        payload={"normal_member_uuid":self.member_uuid}
        result = self.requests.interface_requests_payload(self.member_uuid,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
  #
  # #-------------------第三方平台账户--------------------------------
  #   def testcase_002(self):
  #       sheet_index = 0
  #       row = 144
  #       print("testcase_002 第三方平台账户：")
  #       payload={"normal_member_id":1295}
  #       result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
  #       self.assertEqual(10000, result['code'])
  #       print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()