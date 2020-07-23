# -*- coding:UTF-8 -*-
import unittest
import requests,gc
import sys
import json
import time,xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests


#---------------feed动态删除功能----------------------
class PostsDetail(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------删除自己的动态----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 21
        print("testcase_001动态删除：")

        #调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"uid": "744", "content": "接口在" + date + "测试发布纯文字"}
        # 获取发布接口token值
        member_id = "744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        post_id=result1["data"]["post_id"]

        payload = {"post_id": post_id}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

   #-----------------删除别人的动态----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 22
        print("testcase_002删除别人的动态：")
        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"uid": "744", "content": "接口在" + date + "测试发布纯文字"}
        member_id = "744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        post_id = result1["data"]["post_id"]
        payload ={"post_id": post_id}
        # 获取token值
        member_id = "748"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10003, result["code"])
        print("code返回值：10003")

    #-----------------删除不存在的动态----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 23
        print("testcase_003删除不存在的动态：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

if __name__=="__main__":
    unittest.main()