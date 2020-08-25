# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------群聊邀请向低版本用户发送升级消息---------------------
class Message(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------群聊邀请向低版本用户发送升级消息---------------------------------
    def testcase_001(self):
        sheet_index = 5
        row = 20
        print("testcase_001 群聊邀请向低版本用户发送升级消息：")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        member_uuid = ('85ed3766-7b44-4bf5-a736-bd397de4eed7','e51ae55c-6131-4d20-a31e-6595a932c84b',)
        member_uuid = json.dumps(member_uuid)
        payload = {'member_uuid':member_uuid}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()