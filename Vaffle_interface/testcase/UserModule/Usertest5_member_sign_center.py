# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys

#------------------------用户个人信息---------------------------
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url


class MemberInfo(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------查看存在的当前用户信息，is_verify邮箱是否已经验证 1:是 0:否----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 5
        print("testcase001查看当前用户信息：")
        payload={"member_id":self.member_uuid}
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()
