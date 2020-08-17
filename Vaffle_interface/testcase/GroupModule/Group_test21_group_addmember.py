# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------加入，退出群组----------------------
class InvitedMemberList(unittest.TestCase):

    def setUp(self):
        self.r=FuncRequests()

    #-----------------加入群组---------------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 26
        member_id = '0c6fd624-5b6f-47d2-a91b-e17e992bf056'

        payload = {'guid':'48afaa46-0d80-4518-a880-3577530440d0','type':'add'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------退出群组---------------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 27
        member_id = '0c6fd624-5b6f-47d2-a91b-e17e992bf056'

        payload = {'guid':'48afaa46-0d80-4518-a880-3577530440d0','type':'delete'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
if __name__ == '__main__':
    unittest.main()