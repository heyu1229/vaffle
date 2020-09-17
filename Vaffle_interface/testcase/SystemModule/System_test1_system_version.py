# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys

#------------------------用户个人中心---------------------------

from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------新版本检测----------------------
from Vaffle_interface.public_1.get_version import Version


class System_version(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
        self.version = Version.test_version(self)

    #-----------------新版本检测----------------------------------
    def testcase_001(self):
        # url2 =self.url+"/interservice/version"
        # r = requests.post (url2)
        sheet_index = 3
        row = 1
        print("testcase_001新版本检测：")
        result=self.requests.interface_requests(self.member_uuid,sheet_index,row)

        if self.version =="4.0.8":
            self.assertEqual(10033, result["code"])
            print("code返回值：10033，No new version")
        else :
            self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()