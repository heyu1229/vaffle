# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------签到 - 用户补签----------------------
class Sign(unittest.TestCase):

    def setUp(self):
        self.requests = FuncRequests ()
        self.member_id = '959'

    #-----------------签到 - 用户补签小于当天日期 ，该日期未签到过----------------------------------
    def testcase_001(self):
        #-----用户注册-----
        self.member_id = 'none'
        self.requests = FuncRequests ()
        sheet_index = 0
        row = 12
        print ( "testcase001 用户注册成功:" )
        nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        nickname = 'heyu' + nowTime
        email = 'heyu' + nowTime + '@qq.com'
        print ( email )
        payload = {'email': email, 'password': 'aaa111', 'displayname': 'heyu', 'nickname': nickname,
                   'equipment_number': 'PE-TL10', }
        result = self.requests.interface_requests_payload ( self.member_id, sheet_index, row, payload )
        print(result)
        self.member_id = str(result['data']['member_id'])
        sheet_index = 0
        row = 133
        print("testcase_001签到 用户补签：")
        payload = {'date':'2019-01-06'}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------签到 - 用户补签小于当天日期 ，该日期已签到过---------------------------------
    def testcase_002(self):
        sheet_index = 0
        row = 134
        print("testcase_002签到 用户补签：")
        payload = {'date':'2019-01-06'}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10123, result['code'])
        print("code返回值：10123")

    #-----------------签到 - 用户补签大于当天日期 ，该日期已签到过---------------------------------
    def testcase_002(self):
        sheet_index = 0
        row = 135
        print("testcase_003签到 用户补签：")
        payload = {'date':'2019-1-6'}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10123, result['code'])
        print("code返回值：10123")
        print("msg:此日期不在 允许的范围内，不可补签")


if __name__ == "__main__":
    unittest.main()