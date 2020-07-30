# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------签到 - 用户补签----------------------
class Sign_retrieve(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    #-----------------签到 - 用户补签小于当天日期 ，该日期未签到过----------------------------------
    def testcase_001(self):
        #-----用户注册-----
        self.member_id = 'none'
        self.requests = FuncRequests ()
        sheet_index = 0
        row = 2
        print ( "testcase001 用户注册成功:" )
        nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        nickname = 'heyu' + nowTime
        email = 'heyu' + nowTime + '@qq.com'
        print ( email )
        payload = {'email': email, 'password': 'aaa111', 'displayname': 'heyu', 'nickname': nickname,
                   'equipment_number': 'PE-TL10', }
        result = self.requests.interface_requests_payload ( self.member_id, sheet_index, row, payload )
        print(result)
        self.member_uuid = str(result['data']['member_uuid'])
        sheet_index = 0
        row = 44
        print("testcase_001签到 用户补签：")
        payload = {'date':'2020-07-26'}
        result = self.requests.interface_requests_payload(self.member_uuid,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    def testcase_001(self):
        sheet_index = 0
        row = 44
        print ( "testcase_001签到基础状态信息：" )
        payload = {"dates":"[\"2020-07-29\"]"}
        print(payload)
        result = self.requests.interface_requests_payload ( self.member_uuid, sheet_index, row,payload )
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
    # #-----------------签到 - 用户补签小于当天日期 ，该日期已签到过---------------------------------
    # def testcase_002(self):
    #     sheet_index = 0
    #     row = 134
    #     print("testcase_002签到 用户补签：")
    #     payload = {'date':'2019-01-06'}
    #     result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
    #     self.assertEqual(10123, result['code'])
    #     print("code返回值：10123")
    #
    # #-----------------签到 - 用户补签大于当天日期 ，该日期已签到过---------------------------------
    # def testcase_002(self):
    #     sheet_index = 0
    #     row = 135
    #     print("testcase_003签到 用户补签：")
    #     payload = {'date':'2019-1-6'}
    #     result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
    #     self.assertEqual(10123, result['code'])
    #     print("code返回值：10123")
    #     print("msg:此日期不在 允许的范围内，不可补签")


if __name__ == "__main__":
    unittest.main()