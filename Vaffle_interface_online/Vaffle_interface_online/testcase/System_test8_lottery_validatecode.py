# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc
import json

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------抽奖活动 - 邀请码验证----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

 # -----------------抽奖活动 - 不可以使用自己的邀请码----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 12
        print("testcase_001抽奖活动 - 不可以使用自己的邀请码：")
        member_id = "714"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10102, result["code"])
        print("code返回值：10102")

 # -----------------抽奖活动 - 老用户不能参与抽奖----------------------------------
    def testcase_002(self):
        sheet_index = 3
        row = 13
        print("testcase_002抽奖活动 - 老用户不能参与抽奖：")
        member_id = "714"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10100, result["code"])
        print("code返回值：10100")

 # -----------------抽奖活动 - 新用户参与抽奖----------------------------------
    def testcase_003(self):
        sheet_index = 3
        row = 14
        # 先调用注册接口重新注册一个用户
        nowTime = time.strftime("%Y%m%d_%H_%M_%S")
        nickname = 'test' + nowTime
        email = 'test' + nowTime + '@qq.com'
        print(email)
        member_id1 = 'none'
        payload1 = {'email': email, 'password': 'aaa111', 'displayname': 'test', 'nickname': nickname,
                    'equipment_number': 'PE-TL10', }
        urlpart1 = '/sign/up'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        print(result1)
        global member_id
        member_id = str(result1["data"]["member_id"])
        print("member_id=", member_id)

        print("testcase_003抽奖活动 - 新用户参与抽奖：")
        member_id = member_id
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

 # -----------------抽奖活动 - 邀请码不存在----------------------------------
    def testcase_004(self):
        sheet_index = 3
        row = 15
        print("testcase_004抽奖活动 - 邀请码不存在：")
        member_id = "714"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10103, result["code"])
        print("code返回值：100103")

 # -----------------抽奖活动 - 已抽奖用户不能参与抽奖----------------------------------
    def testcase_005(self):
        sheet_index = 3
        row = 16
        print("testcase_005抽奖活动 - 已抽奖用户不能参与抽奖：")
        member_id = "4361"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10100, result["code"])
        print("code返回值：10100")

if __name__=="__main__":
    unittest.main()