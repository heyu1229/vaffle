# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------签到 - 用户签到----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------签到 - 用户签到 ----------------------------------
    def testcase_001(self):
        #-----用户注册-----
        # self.member_id = 'none'
        # self.requests = FuncRequests ()
        # sheet_index = 0
        # row = 2
        # print ( "testcase001 用户注册成功:" )
        # nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        # nickname = 'heyu' + nowTime
        # email = 'heyu' + nowTime + '@qq.com'
        # print ( email )
        # payload = {'email': email, 'password': 'aaa111', 'displayname': 'heyu', 'nickname': nickname,
        #            'equipment_number': 'PE-TL10', }
        # result = self.requests.interface_requests_payload ( self.member_id, sheet_index, row, payload )
        # print(result)
        # self.member_id = str(result['data']['member_id'])

        sheet_index = 0
        row = 45
        print("testcase_001签到 用户签到：")
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)

        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10125, result['code'])
            print("msg：You had checked in on this date. You can’t check in again.")




if __name__ == "__main__":
    unittest.main()