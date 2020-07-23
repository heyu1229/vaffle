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

#---------------动态详情----------------------
class PostsDetail(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------评论详情----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 55
        print("testcase_001评论详情：")

        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布纯文字"}
        member_id1 = "748"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        post_id = result1["data"]["post_id"]

        # 2.调用评论接口
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload2 = {"post_id": post_id, "content": "接口在" + date + "测试发布评论", "is_post": "N"}
        urlpart2 = '/comments/publish'
        result2 = self.r.interface_requests_data(member_id1, urlpart2, payload2)
        global comment_id
        comment_id = result2["data"]["comment_id"]

        # 3.调用评论详情接口
        payload ={'page':1,'comment_id':comment_id,'direct_id':0}
        # 获取token值
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

   # -----------------评论跳转----------------------------------

    def testcase_002(self):
        sheet_index = 1
        row = 56
        print("testcase_002评论跳转：")
        payload = {'page': 1, 'comment_id': comment_id, 'direct_id': comment_id}
        # 获取token值
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()