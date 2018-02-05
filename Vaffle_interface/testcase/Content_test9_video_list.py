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
#---------------播放视频列表----------------------
class VideoList(unittest.TestCase):

    def setUp(self):
        # 获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        #路径
        self.url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(1, 17, 4,self.filename)
        self.base_url1 = self.url + self.base_url# 获取EXcel路径
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()


    #-----------------播放视频列表latest----------------------------------
    def testcase_001(self):

        sheet_index = 1
        row = 31
        print("testcase_006发布视频动态：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布视频","video": "posts/149673555108234_748_ios.mp4",
                   "video_cover":"posts/149673555108234_748_ios.jpg"}
        member_id="744"
        token = Token().test_token1(payload,member_id)

        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.url+"/posts/publish",params=payload,headers=headers)
        result = r.json()
        post_id =result["data"]["post_id"]

        sheet_index = 1
        row = 17
        print("testcase_001播放视频列表latest：")
        payload = {"post_id": post_id,"page": "1","type": "latest"}
        # 获取token值
        member_id = "744"
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
        self.obj.write_excel_data(sheet_index, row, 7, 'ok',self.path,self.filename)



    #-----------------播放视频列表hot----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 31
        print("testcase_006发布视频动态：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"uid": "744","content": "接口在" + date + "测试发布视频","video": "posts/149484012542459_449_ios.mp4"}
        member_id="744"
        token = Token().test_token1(payload,member_id)

        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.url+"/posts/publish",params=payload,headers=headers)
        result = r.json()
        post_id =result["data"]["post_id"]

        sheet_index = 1
        row = 18
        print("testcase_002播放视频列表hot：")
        payload ={"uid": "744","post_id": post_id,"page": "1","type": "hot"}
        # 获取token值
        member_id = "744"
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
        self.obj.write_excel_data(sheet_index, row, 7, 'ok',self.path,self.filename)


if __name__=="__main__":
    unittest.main()