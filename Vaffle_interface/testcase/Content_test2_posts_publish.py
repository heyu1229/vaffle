#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import json
import time,gc,xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
#---------------发布动态----------------------
class Publish(unittest.TestCase):

    def setUp(self):

        # 获取EXcel路径
        self.path = Url ().test_path ()
        self.filename = "aa"
        #路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(1, 2, 4,self.filename)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()

    #-----------------发布文字动态----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 2
        print("testcase_001发布文字动态：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"content": "接口在"+date+"测试发布纯文字"}
        # 获取token值
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)

        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end-start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


    # -----------------发布空内容----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 27
        print("testcase_002发布空内容：")
        payload = {"content": ""}
        # 获取token值
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end-start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10011, result["code"])
        print("code返回值：10011")
        self.assertEqual("Content cannot be empty.", result["msg"])
        print("msg返回值：Content cannot be empty.")

    #-----------------发布图片动态----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 28
        print("testcase_003发布图片动态：")
        obj = ({"path":"posts/1512710644871_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在"+date+"测试发布图片","images": images}
        # 获取token值
        print(payload)
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end-start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        self.assertEqual("", result["msg"])
        print("msg返回值：ok")

       # -----------------发布九张图片动态----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 29
        print("testcase_004发布九张图片动态：")
        obj = ({"path":"posts/1512710644871_767_android.jpg","ratio":1.23,"tag":1},
               {"path":"posts/1512710644871_767_android.jpg","ratio":1.23,"tag":1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"uid": "744", "content": "接口在" + date + "测试发布九张图片", "images": images}
        # 获取token值
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end-start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.assertEqual("", result["msg"])
        print("msg返回值：ok")

    # -----------------发布纯图片动态----------------------------------
    def testcase_005(self):
        sheet_index = 1
        row = 30
        print("testcase_005发布纯图片动态：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"uid": "744", "images": images}
        # 获取token值
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end-start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------发布视频动态----------------------------------
    def testcase_006(self):
        sheet_index = 1
        row = 31
        print("testcase_006发布视频动态：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布视频","video": "posts/1505153294565_832_android.mp4",
                   "video_cover":'posts/1505153294565_832_android.jpg',"video_cover_ratio":1.00}
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


    # -----------------发布纯视频动态----------------------------------
    def testcase_007(self):
        sheet_index = 1
        row = 32
        print("testcase_007发布纯视频动态：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "video": "posts/149673555108234_748_ios.mp4","video_cover":"posts/149673555108234_748_ios.jpg",
                    "video_cover_ratio":1.00}
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------发布动态+定位----------------------------------
    def testcase_008(self):
        sheet_index = 1
        row = 33
        print("testcase_008发布动态+定位：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布动态+定位","publish_addr":"shanghai"}
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------发布动态+@----------------------------------
    def testcase_009(self):
        sheet_index = 1
        row = 34
        print("testcase_009发布动态+@：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布@queen 动态"}
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------发布动态+#----------------------------------
    def testcase_010(self):
        sheet_index = 1
        row = 35
        print("testcase_010发布动态+#：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj = ("posts/head_male1.jpg",)
        images = json.dumps(obj)
        payload = {"content": "接口在" + date + "测试发布#topic 动态"}
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------发布错误的视频格式----------------------------------
    def testcase_011(self):
        sheet_index = 1
        row = 44
        print("testcase_011发布错误的视频格式：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "发布错误的视频格式","video": "posts/149484012542459_449_ios.mp"}
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10003, result["code"])
        print("code返回值：10003")

    #-----------------发布不存在的视频动态----------------------------------
    def testcase_012(self):
        sheet_index = 1
        row = 45
        print("testcase_012发布不存在的视频动态：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布视频","video": "post/149484012542459_449_ios.mp4"}
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10003, result["code"])
        print("code返回值：10003")


  #-----------------发布错误的图片格式动态----------------------------------
    def testcase_013(self):
        sheet_index = 1
        row = 46
        print("testcase_013发布错误的图片格式动态：")
        obj = ({"path": "posts/1512710644881_767_android.jp", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在"+date+"发布错误的图片格式动态","images": images}
        # 获取token值
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10003, result["code"])
        print("code返回值：10003")


 # #-----------------发布不存在的图片动态----------------------------------
    def testcase_014(self):
        sheet_index = 1
        row = 47
        print("testcase_014发布不存在的图片动态：")
        obj = ({"path":"111posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在"+date+"发布不存在的图片动态","images": images}
        # 获取token值
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10003, result["code"])
        print("code返回值：10003")

   #-----------------发布图片+视频动态----------------------------------
    def testcase_015(self):
        sheet_index = 1
        row = 48
        print("testcase_015发布图片+视频动态：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload = {"content": "接口在" + date + "测试发布图片+视频","video": "posts/149484012542459_449_ios.mp4","images": images}
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result = r.json()
        format_result = json.dumps ( result, indent=1 )
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10012, result["code"])
        print("code返回值：10012")

        # -----------------发布普通图+gif图+长图+live图--------------------------------

    def testcase_016(self):
        sheet_index = 1
        row = 50
        print("testcase_015发布普通图+gif图+长图+live图：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/meinv1.gif ", "ratio": 1.23, "tag": 2},
               {"path": "posts/lang.jpg", "ratio": 1.23, "tag": 3},)
        images = json.dumps(obj)
        payload = {"content": "接口在" + date + "测试发布图片+视频", "images": images}
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"], self.path, self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start, self.path, self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"], self.path, self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767], self.path, self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:], self.path, self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result, self.path, self.filename)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()