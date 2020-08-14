# -*- coding:UTF-8 -*-
import unittest,time
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------首页news列表和用户中心的review列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------首页news列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 41
        print("testcase_001 首页news列表第一页数据：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result = self.r.interface_requests(member_id, sheet_index, row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------用户中心的review列表数据----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 42
        print("testcase_003 用户中心的review列表数据：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result = self.r.interface_requests(member_id, sheet_index, row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()