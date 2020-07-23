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


#---------------举报动态----------------------
class PostsReport(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------举报动态----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 14
        print("testcase_001举报动态：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"uid": "744", "content": "接口在" + date + "测试发布纯文字"}
        # 获取发布接口token值
        member_id1 = "748"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        global post_id
        post_id = result1["data"]["post_id"]

        payload ={"post_id": post_id,"reason_id": "1"}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------二次举报动态----------------------------------
    def testcase_002(self):
        print(post_id)
        sheet_index = 1
        row = 15
        print("testcase_002二次举报动态：")
        payload = {"post_id": post_id,"reason_id": "1"}
        # 获取token值
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10014, result["code"])
        print("code返回值：10014")

if __name__=="__main__":
    unittest.main()