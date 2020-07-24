# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


#------------------------修改用户资料---------------------------
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url


class MemberProfile(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()

    #-----------------修改用户资料,gender:用户性别 M:男 F:女 N:保密----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 6
        print("testcase001修改用户资料：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()