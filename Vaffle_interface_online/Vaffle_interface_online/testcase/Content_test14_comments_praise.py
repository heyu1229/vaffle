#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc,xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------评论点赞/取消点赞----------------------
class Praise(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------评论点赞----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 53
        print("testcase_001评论点赞：")

        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = { "content": "接口在" + date + "测试发布纯文字"}
        member_id1 = "748"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        post_id = result1["data"]["post_id"]

        # 2.调用评论接口，获得comment_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload2 = {"post_id": post_id, "content": "接口在" + date + "测试发布评论", "is_post": "N"}
        urlpart2 = '/comments/publish'
        result2 = self.r.interface_requests_data(member_id1, urlpart2, payload2)
        global comment_id
        comment_id = result2["data"]["comment_id"]
        print(comment_id)

        #3.调用评论点赞接口
        payload ={"comment_id": comment_id,'praise_state':1}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
    #-----------------取消点赞----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 54
        print("testcase_002取消点赞：")
        # 调用评论点赞接口
        payload = {"comment_id": comment_id,'praise_state':0}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
