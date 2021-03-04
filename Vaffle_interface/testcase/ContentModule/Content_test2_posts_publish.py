#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import json
import time,gc,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------发布动态----------------------
class Publish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------发布图片动态----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 2
        print("testcase_001发布图片动态：")
        obj = ({"path":"posts/1512710644871_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        print(images)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在"+date+"#SantaSide 测试发布图片","images": images,"category":"post"}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        # member_id = "176cfef2-007f-4b3b-8089-1d438ec3d06a"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        print(result)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

       # -----------------发布九张图片动态----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 3
        print("testcase_002发布九张图片动态：")
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
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


    #-----------------发布视频动态----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 4
        print("testcase_003发布视频动态：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content": "接口在" + date + "测试发布视频","video": "posts/1505153294565_832_android.mp4",
                   "video_cover":'posts/1505153294565_832_android.jpg',"video_cover_ratio":1.00}
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布review--------------------------------
    #[{"androidid":"1532313356301","imageUrl":"https://s3-us-west-2.amazonaws.com/images-omv/posts/1532313355871_767_android.jpg","radio":"1.0000","tag":1}]
    def testcase_004(self):
        sheet_index = 1
        row = 5
        print("testcase_004发布review：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj = ({"path":"https://s3-us-west-2.amazonaws.com/images-omv/posts/1532313355871_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content":"评测内容","category":"review","review_title":"接口在"+date+"发布review","review_product":"测评产品","review_type":"测评产品型号","publish_addr":"111"}
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        result=self.r.interface_requests_payload_apitest2(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布QA------------------------------
    def testcase_005(self):
        sheet_index = 1
        row = 6
        print("testcase_005发布QA：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"QA内容1"+date,"category":"qa","goods_id":2675}
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布群组post------------------------------
    def testcase_006(self):
        sheet_index = 1
        row = 7
        print("testcase_006发布群组post：")
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"发布群组post"+date,"category":"post","guid":"c3172313-243f-4752-8ee9-10a1faa2ef6e"}
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布标签------------------------------
    def testcase_007(self):
        sheet_index = 1
        row = 103#"category":1,"params":"b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        print("testcase_007 发布标签：")
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1,
                "imageTags":[{"proportionX":0.5,"proportionY":0.1,"direction":1,"title":"texttag003","tagType":3,"category":0,"params":"text:texttag003"},
                             {"proportionX":0.5,"proportionY":0.3,"direction":1,"title":"usertag003","tagType":3,"category":1,"params":"member:b9f73f23-7bc6-4de6-9f9b-df2c98076221"},
                             {"proportionX":0.5,"proportionY":0.5,"direction":1,"title":"goodstag003","tagType":3,"category":2,"params":"goods:2675"},
                             {"proportionX":0.5,"proportionY":0.7,"direction":1,"title":"testbrand003","tagType":3,"category":3,"params":"brand:179"}]
                },)
        images = json.dumps(obj)
        print(images)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"发布标签"+date,"category":"post"}
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()