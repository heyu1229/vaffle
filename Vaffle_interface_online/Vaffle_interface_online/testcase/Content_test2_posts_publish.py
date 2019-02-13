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
        payload = {"content": "接口在" + date + "测试发布图片+视频", "images": images}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


    # -----------------发布review--------------------------------
    #[{"androidid":"1532313356301","imageUrl":"https://s3-us-west-2.amazonaws.com/images-omv/posts/1532313355871_767_android.jpg","radio":"1.0000","tag":1}]
    def testcase_016(self):
        sheet_index = 1
        row = 98
        print("testcase_016发布review：")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj = ({"path":"https://s3-us-west-2.amazonaws.com/images-omv/posts/1532313355871_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"content":"评测内容","category":"review","review_title":"接口在"+date+"发布review","review_product":"测评产品","review_type":"测评产品型号","publish_addr":"111"}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布QA------------------------------
    def testcase_017(self):
        sheet_index = 1
        row = 99
        print("testcase_017发布QA：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"uid": "744", "images": images, "content":"QA内容1"+date,"category":"qa"}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布想法------------------------------
    def testcase_018(self):
        sheet_index = 1
        row = 102
        print("testcase_018发布想法：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"接口测试发布想法"+date,"category":"post","topic_id":40}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------发布店铺评论------------------------------
    def testcase_019(self):
        sheet_index = 1
        row = 103
        print("testcase_019发布店铺评论：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"接口测试发布店铺评论"+date,"category":"post","shop_id":1315}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------管理员身份发布post并推送给粉丝------------------------------
    def testcase_020(self):
        sheet_index = 1
        row = 104
        print("testcase_020管理员身份发布post并推送给粉丝：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"管理员身份发布post并推送给粉丝"+date,"normal_member_id":745,"push":"ON"}
        member_id = "10394"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------切换管理员身份发布post------------------------------34791
    def testcase_021(self):
        sheet_index = 1
        row = 105
        print("testcase_021切换管理员身份发布post：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"切换管理员身份发布post"+date,"target_role":10394,"normal_member_id":745}
        member_id = "745"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------切换普通身份发布post------------------------------34791
    def testcase_022(self):
        sheet_index = 1
        row = 106
        print("testcase_022切换普通身份发布post：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"切换普通身份发布post"+date,"target_role":745,"normal_member_id":745}
        member_id = "10394"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------切换其他管理员身份发布post------------------------------34791
    def testcase_023(self):
        sheet_index = 1
        row = 107
        print("testcase_023切换其他管理员身份发布post：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"切换其他管理员身份发布post"+date,"target_role":34791,"normal_member_id":745}
        member_id = "10394"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    # -----------------管理员发布QA------------------------------
    def testcase_024(self):
        sheet_index = 1
        row = 108
        print("testcase_024管理员发布QA：")
        obj = ({"path":"posts/1512710644881_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = { "images": images, "content":"管理员发布QA"+date,"category":"qa","target_role":10394,"normal_member_id":745}
        member_id = "745"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()