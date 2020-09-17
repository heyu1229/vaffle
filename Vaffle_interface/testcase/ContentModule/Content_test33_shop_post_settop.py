# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------设置店铺置顶post数据----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------设置店铺置顶post数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 46
        print("testcase_001 设置店铺置顶post数据：")

        member_id = "7238fc91-0b5e-4f14-8288-95f60dae7658"
        payload = {"normal_member_uuid":"b9f73f23-7bc6-4de6-9f9b-df2c98076221","state": 1, "post_id": 89534}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # -----------------设置店铺取消置顶post数据----------------------------------

    def testcase_002(self):
        sheet_index = 1
        row = 47
        print("testcase_002 设置店铺取消置顶post数据：")

        member_id = "7238fc91-0b5e-4f14-8288-95f60dae7658"
        payload = {"normal_member_uuid": "b9f73f23-7bc6-4de6-9f9b-df2c98076221", "state": 0, "post_id": 89534}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()