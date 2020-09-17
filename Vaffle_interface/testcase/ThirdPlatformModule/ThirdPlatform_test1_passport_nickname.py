# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys

#------------------------用户个人中心---------------------------

from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------检测第三方是否注册【POST】----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()

    #-----------------	检测第三方已注册----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 1
        print("testcase_001检测第三方已注册：")
        member_id='none'
        result=self.requests.interface_requests(self.member_uuid,sheet_index,row)
        data=result['data']
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        self.assertEqual(5, len(data["list"]))
        print("推荐的用户昵称等于1，表示已经注册")





if __name__=="__main__":
    unittest.main()
