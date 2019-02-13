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
from func_requests import FuncRequests

#---------------发布评论----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------发布评论----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 11
        print("testcase_001发布评论：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"uid": "744", "content": "接口在" + date + "测试发布纯文字"}
        member_id1 = "748"
        urlpart = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)
        global post_id
        post_id = result1["data"]["post_id"]


        payload = {"post_id": post_id,"content": "接口在"+date+"测试发布评论","is_post":"N"}
        member_id="423"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        global comment_id
        comment_id = result["data"]["comment_id"]

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # -----------------发布空评论----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 36
        print("testcase_002发布空评论：")
        payload = {"post_id": post_id, "content": "", "is_post": "N"}
        # 获取token值
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

    #-----------------回复评论----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 37
        print("testcase_003回复评论:")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"post_id": post_id, "content": "接口在" + date + "测试回复评论","is_post": "N", "reply_id": comment_id}
        # 获取token值
        member_id="423"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------发布评论并转发----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 38
        print("testcase_004发布评论并转发:")
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"post_id": post_id, "content": "接口在" + date + "测试发布评论并转发", "is_post": "Y"}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------发布评论+@----------------------------------
    def testcase_005(self):
        sheet_index = 1
        row = 39
        print("testcase_005发布评论+@：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"post_id": post_id,"content": "接口在"+date+"测试发布@tester 评论","is_post":"N"}
        # 获取token值
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------发布评论+#----------------------------------
    def testcase_006(self):
        sheet_index = 1
        row = 40
        print("testcase_006发布评论+#：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"post_id": post_id,"content": "接口在"+date+"测试发布#topic 评论","is_post":"N"}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()