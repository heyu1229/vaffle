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
        self.base_url = self.obi.read_excel_data(1, 57, 4,self.filename)
        self.base_url1 = self.url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()

    #-----------------post点赞记录列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 57
        print("testcase_001post点赞记录列表：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布纯文字"}
        member_id1 = "748"
        token1 = Token().test_token1(payload1, member_id1)
        headers1 = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                    "token": token1,
                    "login": member_id1}
        r1 = requests.post(self.url + "/posts/publish", params=payload1, headers=headers1)
        result1 = r1.json()
        post_id = result1["data"]["post_id"]

        # 调用动态点赞接口
        payload2 = {"post_id": post_id, "praise_state": 1}
        # 获取token
        member_id = "744"
        token2 = Token().test_token1(payload2, member_id)
        headers2 = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token2,
                   "login": member_id}
        r2 = requests.post(self.url + "/posts/praise", params=payload2, headers=headers2)
        result2 = r2.json()

        #调用动态点赞列表接口
        payload ={'page':1,'post_id':post_id}
        # 获取token值
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


if __name__=="__main__":
    unittest.main()