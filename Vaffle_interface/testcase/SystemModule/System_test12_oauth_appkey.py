# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------获取开放接口oauth授权认证信息----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

 # -----------------获取开放接口oauth授权认证信息----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 20
        print("testcase_001获取开放接口oauth授权认证信息：")
        result=self.requests.interface_requests(self.member_uuid,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

 # # -----------------更新开放接口oauth授权认证信息----------------------------------
 #    def testcase_002(self):
 #        sheet_index = 3
 #        row = 21
 #        print("testcase_001更新开放接口oauth授权认证信息：")
 #        member_id = "745"
 #        result=self.r.interface_requests(member_id,sheet_index,row)
 #
 #        self.assertEqual(10000, result["code"])
 #        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()