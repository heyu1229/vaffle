# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------群组邀请搜索----------------------
class InvitedMemberList(unittest.TestCase):

    def setUp(self):
        self.r=FuncRequests()

    #-----------------群组邀请搜索---------------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 20
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'

        payload = {'type':'invite','keywords':'queen','page':1,'guid':'48afaa46-0d80-4518-a880-3577530440d0'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------groupmeber搜索---------------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 21
        member_id = 'e51ae55c-6131-4d20-a31e-6595a932c84b'

        payload = {'type':'groupmeber','keywords':'queen','page':1,'guid':'48afaa46-0d80-4518-a880-3577530440d0'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == '__main__':
    unittest.main()