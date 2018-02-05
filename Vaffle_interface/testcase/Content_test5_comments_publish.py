# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import json
import time

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData

#---------------发布评论----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):

        #路径
        self.path = Url ().test_path ()
        self.filename = "aa"
        #路径
        self.url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(1, 11, 4,self.filename)
        self.base_url1 = self.url + self.base_url

        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------发布评论----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 11
        print("testcase_001发布评论：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"uid": "744", "content": "接口在" + date + "测试发布纯文字"}
        # 获取发布接口token值
        member_id1 = "748"
        token1 = Token().test_token1(payload1, member_id1)

        headers1 = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token1,
                    "login": member_id1}
        r1 = requests.post(self.url+"/posts/publish", params=payload1, headers=headers1)
        result1 = r1.json()
        global post_id
        post_id = result1["data"]["post_id"]


        payload = {"post_id": post_id,"content": "接口在"+date+"测试发布评论","is_post":"N"}
        # 获取token值
        member_id="423"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        print(result)
        end = time.time()
        global comment_id
        comment_id = result["data"]["comment_id"]

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

        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


        # -----------------发布空评论----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 36
        print("testcase_002发布空评论：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"post_id": post_id, "content": "", "is_post": "N"}
        # 获取token值
        member_id="744"
        token = Token().test_token1(payload,member_id)

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


        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

        self.assertEqual("Time out.", result["msg"])
        print("msg返回值：Time out.")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


    #-----------------回复评论----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 37
        print("testcase_003回复评论:")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"post_id": post_id, "content": "接口在" + date + "测试回复评论","is_post": "N", "reply_id": comment_id}
        # 获取token值
        member_id="423"
        token = Token().test_token1(payload,member_id)

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

        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


    #-----------------发布评论并转发----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 38
        print("testcase_004发布评论并转发:")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"post_id": post_id, "content": "接口在" + date + "测试发布评论并转发", "is_post": "Y"}
        # 获取token值
        member_id="744"
        token = Token().test_token1(payload,member_id)
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

        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


    #-----------------发布评论+@----------------------------------
    def testcase_005(self):
        sheet_index = 1
        row = 39
        print("testcase_005发布评论+@：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"post_id": post_id,"content": "接口在"+date+"测试发布@tester 评论","is_post":"N"}
        # 获取token值
        member_id="744"
        token = Token().test_token1(payload,member_id)

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

        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


    #-----------------发布评论+#----------------------------------
    def testcase_006(self):
        sheet_index = 1
        row = 40
        print("testcase_006发布评论+#：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"post_id": post_id,"content": "接口在"+date+"测试发布#topic 评论","is_post":"N"}
        # 获取token值
        member_id="744"
        token = Token().test_token1(payload,member_id)

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

        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


if __name__ == "__main__":
    unittest.main()