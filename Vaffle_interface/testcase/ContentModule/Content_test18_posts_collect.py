# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc,xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------动态收藏/取消收藏----------------------
class CommentsLists(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------动态收藏----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 60
        print("testcase_001评论列表:")
        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = { "content": "接口在" + date + "测试发布纯文字"}
        member_id1 = "748"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        global post_id
        post_id = result1["data"]["post_id"]
        print(post_id)

        #2.调用动态收藏/取消收藏接口
        payload = {'post_id': post_id, 'state': 1}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------取消收藏----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 61
        payload = {'post_id': post_id, 'state': 0}
        member_id = "744"
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
