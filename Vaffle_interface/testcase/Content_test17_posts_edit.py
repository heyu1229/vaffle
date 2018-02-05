# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc,xlrd
import json
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version

#---------------post点赞记录列表----------------------
class PostsDetail(unittest.TestCase):

    def setUp(self):
        # 获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        #路径
        self.url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(1, 58, 4,self.filename)
        self.base_url1 = self.url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()

    #-----------------动态编辑----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 58
        print("testcase_001动态编辑：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布纯文字"}
        member_id = "744"
        token1 = Token().test_token1(payload1, member_id)
        headers1 = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                    "token": token1,
                    "login": member_id}
        r1 = requests.post(self.url + "/posts/publish", params=payload1, headers=headers1)
        result1 = r1.json()
        post_id = result1["data"]["post_id"]

        #调用动态编辑接口
        payload ={'post_id':post_id,'content':'接口在' + date + '编辑动态'}
        token = Token().test_token1(payload, member_id)
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1, params=payload, headers=headers)
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


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)

        # -----------------编辑别人的动态----------------------------------

    def testcase_002(self):
        sheet_index = 1
        row = 59
        print("testcase_002编辑别人的动态：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布纯文字"}
        member_id = "744"
        token1 = Token().test_token1(payload1, member_id)
        headers1 = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                    "token": token1,
                    "login": member_id}
        r1 = requests.post(self.url + "/posts/publish", params=payload1, headers=headers1)
        result1 = r1.json()
        post_id = result1["data"]["post_id"]

        # 调用动态编辑接口
        payload = {'post_id': post_id, 'content': '接口在' + date + '编辑动态'}
        member_id1 = "748"
        token = Token().test_token1(payload, member_id1)
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token,
                   "login": member_id1}
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

        self.assertEqual(10003, result["code"])
        print("code返回值：10003")
        self.obj.write_excel_data(sheet_index, row, 7, "ok", self.path, self.filename)


if __name__=="__main__":
    unittest.main()