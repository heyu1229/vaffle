# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------------用户的电子烟设备列表  vape_member_vape_device表--------1:正常; 0:删除   2:待审核-------------------
class DeviceList(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------用户的电子烟设备列表   pending,not_passed,verified)----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 17
        print("testcase001 用户的电子烟设备列表：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()