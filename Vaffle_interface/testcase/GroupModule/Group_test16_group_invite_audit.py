# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------群组请求----------------------
class InvitedMemberList(unittest.TestCase):

    def setUp(self):
        self.r=FuncRequests()

    #-----------------同意群组请求---------------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 18
        member_id = 'e51ae55c-6131-4d20-a31e-6595a932c84b'

        payload = {"group_invite_id":3191,'status':1,'ignore_ever':0}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------拒绝群组请求---------------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 19
        member_id = 'e51ae55c-6131-4d20-a31e-6595a932c84b'

        payload = {"group_invite_id":3191,'status':0,'ignore_ever':0}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == '__main__':
    unittest.main()