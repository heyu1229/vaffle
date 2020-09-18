# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------推送通知开关----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    # -----------------推送通知开关----------------------------------
    def testcase_001(self):
        sheet_index = 9
        row = 9
        print("testcase_001 推送通知开关：")
        member_id = '85ed3766-7b44-4bf5-a736-bd397de4eed7'
        timeRange = {"end": "08:00", "start": "00:00", "timezone": "8.0"}
        payload = {'followers':1,'attention':1,'like':1,'comment':1,'newPostByFollowing':1,'newAnswerInFollowQuestion':1,
                   'newPostInGroup':1,'privateMsg':1,'answerMyQuestion':1,'hotRecommend':1,'notDisturbMod':0,
                   'inviteAnswer':1,'timeRange':timeRange}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
