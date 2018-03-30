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
from func_requests import FuncRequests
#---------------发布动态----------------------
class Publish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------发布文字动态----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 2
        print("testcase_001发布文字动态：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"content": "接口在"+date+"测试发布纯文字"}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


    # -----------------发布空内容----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 27
        print("testcase_002发布空内容：")
        payload = {"content": ""}
        member_id='744'
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10011, result['code'])
        print("code返回值：10011")

    #-----------------发布图片动态----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 28
        print("testcase_003发布图片动态：")
        obj = ({"path":"posts/1512710644871_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在"+date+"测试发布图片","images": images}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

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
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布纯图片动态----------------------------------
    def testcase_005(self):
        sheet_index = 1
        row = 30
        print("testcase_005发布纯图片动态：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"uid": "744", "images": images}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
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
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
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
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布动态+定位----------------------------------
    def testcase_008(self):
        sheet_index = 1
        row = 33
        print("testcase_008发布动态+定位：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布动态+定位","publish_addr":"shanghai"}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布动态+@----------------------------------
    def testcase_009(self):
        sheet_index = 1
        row = 34
        print("testcase_009发布动态+@：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布@queen 动态"}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
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
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------发布错误的视频格式----------------------------------
    def testcase_011(self):
        sheet_index = 1
        row = 44
        print("testcase_011发布错误的视频格式：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "发布错误的视频格式","video": "posts/149484012542459_449_ios.mp"}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10003, result['code'])
        print("code返回值：10003")


  #-----------------发布错误的图片格式动态----------------------------------
    def testcase_012(self):
        sheet_index = 1
        row = 46
        print("testcase_013发布错误的图片格式动态：")
        obj = ({"path": "posts/1512710644881_767_android.jp", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在"+date+"发布错误的图片格式动态","images": images}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10003, result['code'])
        print("code返回值：10003")


 # #-----------------发布不存在的图片动态----------------------------------
    def testcase_013(self):
        sheet_index = 1
        row = 47
        print("testcase_014发布不存在的图片动态：")
        obj = ({"path":"111posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在"+date+"发布不存在的图片动态","images": images}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10003, result['code'])
        print("code返回值：10003")

   #-----------------发布图片+视频动态----------------------------------
    def testcase_014(self):
        sheet_index = 1
        row = 48
        print("testcase_015发布图片+视频动态：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload = {"content": "接口在" + date + "测试发布图片+视频","video": "posts/149484012542459_449_ios.mp4","images": images}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10012, result['code'])
        print("code返回值：10012")

        # -----------------发布普通图+gif图+长图+live图--------------------------------

    def testcase_015(self):
        sheet_index = 1
        row = 50
        print("testcase_015发布普通图+gif图+长图+live图：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/meinv1.gif ", "ratio": 1.23, "tag": 2},
               {"path": "posts/lang.jpg", "ratio": 1.23, "tag": 3},)
        images = json.dumps(obj)
        payload = {"content": "接口在" + date + "测试发布普通图+gif图+长图+live图", "images": images}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布图片挑战-------------------------------
    def testcase_016(self):
        sheet_index = 1
        row = 63
        print("testcase_016发布图片挑战活动：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/meinv1.gif ", "ratio": 1.23, "tag": 2},
               {"path": "posts/lang.jpg", "ratio": 1.23, "tag": 3},)
        images = json.dumps(obj)
        payload = {"content": "接口在" + date + "测试发布图片挑战活动", "images": images,"challenge":"templarRDA vaping1","challenge_id":1}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布视频挑战-------------------------------
    def testcase_017(self):
        sheet_index = 1
        row = 64
        print("testcase_016发布挑战活动：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布视频挑战活动", "video": "posts/1505153294565_832_android.mp4",
                   "video_cover": 'posts/1505153294565_832_android.jpg', "video_cover_ratio": 1.00,"challenge":"templarRDA vaping1","challenge_id":1}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()