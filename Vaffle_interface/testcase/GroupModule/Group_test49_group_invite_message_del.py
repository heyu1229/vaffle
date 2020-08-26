# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------【群组消息】群组邀请消息删除----------------------
class Group_noticedel(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------【群组消息】群组邀请消息删除--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 60
        print("testcase_001 群组邀请消息删除:")

        #发送邀请
        member_id1='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        member_uuid = '85ed3766-7b44-4bf5-a736-bd397de4eed7'
        payload1 = {"guid":"48afaa46-0d80-4518-a880-3577530440d0","member_uuid":member_uuid}
        urlpart1 = '/group/invite'
        result1 = self.r.interface_requests_data(member_id1,urlpart1,payload1)
        print('result1=',result1)

        #获取邀请id
        member_id2 = '85ed3766-7b44-4bf5-a736-bd397de4eed7'
        payload2 = {"page": "1"}
        urlpart2 = '/group/apply'
        result2 = self.r.interface_requests_data(member_id2,urlpart2,payload2)
        print('result2=',result2)
        group_invite_id = result2['data']['list'][0]['group_invite_id']
        print('group_invite_id=',group_invite_id)

        #删除邀请
        payload = {'group_invite_id':group_invite_id}
        result=self.r.interface_requests_payload(member_id2,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()