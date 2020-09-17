# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------店铺媒体资源列表（网友、官方）----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()
       self.member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

    #-----------------店铺媒体资源列表--网友----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 3
        print ("testcase_001店铺媒体资源列表--网友:")

        result = self.r.interface_requests(self.member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------店铺媒体资源列表--官方----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 4
        print ("testcase_001店铺媒体资源列表--官方:")

        result = self.r.interface_requests(self.member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------店铺媒体资源列表--视频----------------------------------
    def testcase_003(self):
        sheet_index = 12
        row = 5
        print ("testcase_001店铺媒体资源列表--视频:")

        result = self.r.interface_requests(self.member_id, sheet_index, row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()