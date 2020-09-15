# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------第三方登录接口----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------第三方facebook登录成功----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 3
        print("testcase_001第三方facebook登录成功：")
        data = int(time.time())
        member_id = "none"
        payload = {'platform':'facebook','open_id':'587211848358211','nickname':'Luo_Taibin898',
                   'gender':'N','equipment_number':'1589345731','email':'facebook@email'+str(data)+'.com'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

     # -----------------第三方twitter登录成功----------------------------------
    # -----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------

    def testcase_002(self):
        sheet_index = 6
        row = 4
        print("testcase_002第三方twitter登录成功：")
        member_id = "none"
        data = int(time.time())
        payload = {'platform': 'twitter', 'open_id': '1155763404771975169', 'nickname': 'Hhhh869',
                   'gender': 'N', 'equipment_number': '1589257309', 'email': 'twitter@email' + str(data) + '.com'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------第三方vk登录成功----------------------------------
    # -----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_003(self):
        sheet_index = 6
        row = 5
        print("testcase_003第三方vk登录成功：")
        member_id = "none"
        data = int(time.time())
        payload = {'platform': 'vk', 'open_id': '427871220', 'nickname': 'He_Yu874',
                   'gender': 'F', 'equipment_number': '1590730356', 'email': 'vk@email' + str(data) + '.com'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


    # -----------------第三方INS登录成功----------------------------------
    def testcase_005(self):
        sheet_index = 6
        row = 6
        print ( "testcase_005 第三方ins登录成功：" )
        member_id = "none"
        data = int(time.time())
        payload = {'platform': 'instagram', 'open_id': '33471139089', 'nickname': 'derrickvapeer',
                   'gender': 'N', 'equipment_number': '1590730470', 'email': 'instagram@email' + str(data) + '.com'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual ( 10000, result["code"] )
        print ( "code返回值：10000" )

    # -----------------第三方带密码登录----------------------------------
    def testcase_006(self):
        sheet_index = 6
        row = 12
        print ( "testcase_006 第三方带密码登录：" )
        member_id = "35710"
        payload={"platform": "vk", "open_id": "431978087", "nickname": "Qin_Yu503", "gender": "F",
                 "equipment_number": "PE-TL10", "fcm_token": "dn612TZsnqM:APA91bGYxz6qppK5mQexGBUMcFzg3D8Qd7OKOL-zBHwIj5wel3rbfFNvg-cZsyCsJKBvQbejMvWxxK7iIjm24ujBYn_zhnPVbNaisaVvAvC4w_0",
                 "password":111111}
        result = self.r.interface_requests_payload(member_id, sheet_index, row,payload)

        self.assertEqual ( 10000, result["code"] )
        print ( "code返回值：10000" )


if __name__=="__main__":
    unittest.main()
