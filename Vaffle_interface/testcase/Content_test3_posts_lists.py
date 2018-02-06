#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc,xlrd
import json,time
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests
#---------------discover video列表----------------------
class List(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()


    #-----------------首页动态列表post 第1页----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 3
        print("testcase_001首页动态列表post 第1页:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        post_list = result['data']['list']
        global last_id
        last_id = post_list[0]['post_id']

    #-----------------首页动态列表reveal 第1页---------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 4
        print("testcase_002首页动态列表reveal 第1页:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


   #-----------------首页动态列表post 第2页----------------------------------
    def testcase_003(self):

        sheet_index = 1
        row = 5
        print("testcase_003页动态列表post 第2页:")
        member_id="744"
        print('last_id: ',last_id)
        #再根据last_id获得第二页数据
        payload = {'type':'post','page':2,'last_id':last_id}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------获得置顶的post----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 6
        print("testcase_004获得置顶的post:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)
        top=result['data']['top']
        if top=={}:
            print('没有置顶数据')
        else:
            print('有置顶数据:',top)

    # -----------------首页动态列表type不存在----------------------------------
    def testcase_005(self):
        sheet_index = 1
        row = 7
        print("testcase_005首页动态列表type不存在:")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        print(result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(9999, result["code"])
        print("code返回值：9999")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)

        # -----------------discover video列表 第一页---------------------------------

    def testcase_006(self):
        sheet_index = 1
        row = 51
        print("testcase_006discover video列表 第一页:")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5, self.filename)
        # 获取token
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        print(result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"], self.path, self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start, self.path, self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767], self.path, self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:], self.path, self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result, self.path, self.filename)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.obj.write_excel_data(sheet_index, row, 7, "ok", self.path, self.filename)

        # -----------------discover video列表 第2页----------------------------------

    def testcase_007(self):
        sheet_index = 1
        row = 52
        print("testcase_007discover video列表 第2页:")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5, self.filename)
        # 获取token
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        print(result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"], self.path, self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start, self.path, self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767], self.path, self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:], self.path, self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result, self.path, self.filename)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.obj.write_excel_data(sheet_index, row, 7, "ok", self.path, self.filename)


if __name__ == "__main__":
    unittest.main()