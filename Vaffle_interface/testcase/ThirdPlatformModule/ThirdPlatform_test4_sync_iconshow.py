# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------第三方分享回调接口----------------------
from Vaffle_interface.public_1.get_url import Url

#---------------发布时第三方平台图标显示【POST】----------------------
class Sync_iconshow(unittest.TestCase):

    def setUp(self):
        self.requests = FuncRequests()
        self.member_uuid = 'none'

    def testcase_001(self):
        sheet_index = 6
        row = 4
        print("testcase_001发布时第三方平台图标显示")

        payload = {}
        result=self.requests.interface_requests_payload(self.member_uuid, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()
