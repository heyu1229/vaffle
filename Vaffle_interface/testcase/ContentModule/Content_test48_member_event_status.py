# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------兑换礼品/post好评/群组邀请好友 状态值记录----------------------
class member_event_status(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------兑换礼品状态值记录----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 63
        print("testcase_001 兑换礼品状态值记录：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'type':'exchange_thanks_status','status':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------邀请好友状态值记录----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 64
        print("testcase_002 邀请好友状态值记录：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'type':'invite_thanks_status','status':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------完善个人资料隐藏状态值记录----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 65
        print("testcase_003 完善个人资料隐藏状态值记录：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'type':'postPraise_thanks_status','status':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------兑换礼品状态值记录----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 66
        print("testcase_004 兑换礼品状态值记录：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'type':'profile_complete_hide','status':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()