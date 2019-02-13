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
from func_requests import FuncRequests
#---------------播放视频列表----------------------
class VideoList(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------播放视频列表post----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 17
        print("testcase_001播放视频列表post：")
        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布视频","video": "posts/149673555108234_748_ios.mp4",
                   "video_cover":"posts/149673555108234_748_ios.jpg"}
        member_id="744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        post_id =result1["data"]["post_id"]
        print("post_id=",post_id)

        payload = {"post_id": post_id,"page": "1","type": "post"}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------播放视频列表reveal----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 18
        print("testcase_002播放视频列表reveal：")
        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布视频", "video": "posts/149673555108234_748_ios.mp4",
                    "video_cover": "posts/149673555108234_748_ios.jpg"}
        member_id = "744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        post_id = result1["data"]["post_id"]

        payload = {"post_id": post_id, "page": "1", "type": "reveal"}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()