# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------管理员移除成员----------------------
class InvitedMemberList(unittest.TestCase):

    def setUp(self):
        self.r=FuncRequests()

    #-----------------管理员移除成员---------------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 25

        member_id1 = 'ad33d861-f31d-4f2e-95f6-acb6ccf34747'
        payload1 = {'guid':'48afaa46-0d80-4518-a880-3577530440d0','type':'add'}
        urlpart1 = '/group/addmember'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        print(result1)

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'guid':'48afaa46-0d80-4518-a880-3577530440d0','type':'delete','member_uuid':'ad33d861-f31d-4f2e-95f6-acb6ccf34747'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()