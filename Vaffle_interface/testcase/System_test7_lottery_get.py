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

#---------------管理我的店铺 - 功能项----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------抽奖活动 - 新用户参与抽奖---------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 8
        #先调用注册接口重新注册一个用户
        nowTime = time.strftime("%Y%m%d_%H_%M_%S")
        nickname = 'test' + nowTime
        email = 'test' + nowTime + '@qq.com'
        print(email)
        member_id1 = 'none'
        payload1 = {'email': email,'password': 'aaa111','displayname': 'test','nickname': nickname,'equipment_number': 'PE-TL10',}
        urlpart1 = '/sign/up'
        result1 = self.r.interface_requests_data(member_id1,urlpart1, payload1)
        print(result1)
        global member_id
        member_id = str(result1["data"]["member_id"])
        print("member_id=",member_id)

        print("testcase_001抽奖活动 - 新用户参与抽奖：")

        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version().test_version()
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5)
        # 获取token值
        base_url0 = Url().test_url() + '/token'
        serial_number = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505',
                   'login': member_id, "serial-number": serial_number, "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "system_version"}
        r = requests.post(base_url0, params=payload, headers=headers)
        content = r.json()
        print(content)
        token = content['token']

        # 记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token,
                   "login": member_id, "serial-number": serial_number, "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "system_version"}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"], self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"], self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767], self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:], self.path)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result, self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start, self.path)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

 # -----------------抽奖活动 - 老用户不能参与抽奖----------------------------------
    def testcase_002(self):
        sheet_index = 3
        row = 9
        print("testcase_002抽奖活动 - 老用户不能参与抽奖：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10100, result["code"])
        print("code返回值：10100")

 #-----------------抽奖活动 - 已抽奖用户不能参与抽奖----------------------------------
    def testcase_003(self):
        sheet_index = 3
        row = 10
        print("testcase_003抽奖活动 - 已抽奖用户不能参与抽奖：")

        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version().test_version()
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5)
        # 获取token值
        base_url0 = Url().test_url() + '/token'
        serial_number = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505',
                   'login': member_id, "serial-number": serial_number, "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "system_version"}
        r = requests.post(base_url0, params=payload, headers=headers)
        content = r.json()
        print(content)
        token = content['token']

        # 记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token,
                   "login": member_id, "serial-number": serial_number, "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "system_version"}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"], self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"], self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767], self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:], self.path)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result, self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start, self.path)

        self.assertEqual(10099, result["code"])
        print("code返回值：10099")

#-----------------抽奖活动 - 用户自己不能使用自己的邀请码进行抽奖----------------------------------
    def testcase_004(self):
        sheet_index = 3
        row = 11

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
        member_id = str(result1["data"]["member_id"])
        print("member_id=", member_id)

        # 先调用个人中心接口获得新注册用户的邀请码

        payload1 = {'member_id': member_id }
        urlpart1 = '/member/center'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        print(result1)
        invite_code = str(result1["data"]["invite_code"])
        print("invite_code=", invite_code)


        print("testcase_004抽奖活动 - 用户自己不能使用自己的邀请码进行抽奖：")

        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version().test_version()
        payload = {'invitation_code':invite_code}
        # 获取token值
        base_url0 = Url().test_url() + '/token'
        serial_number = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505',
                   'login': member_id, "serial-number": serial_number, "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "system_version"}
        r = requests.post(base_url0, params=payload, headers=headers)
        content = r.json()
        print(content)
        token = content['token']

        # 记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token,
                   "login": member_id, "serial-number": serial_number, "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "system_version"}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"], self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"], self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767], self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:], self.path)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result, self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start, self.path)

        self.assertEqual(10102, result["code"])
        print("code返回值：10102")


if __name__=="__main__":
    unittest.main()