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

#---------------评论列表----------------------
class CommentsLists(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------评论列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 12
        print("testcase_001评论列表:")
        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = { "content": "接口在" + date + "测试发布纯文字"}
        member_id1 = "748"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        post_id = result1["data"]["post_id"]

        #2.调用评论接口进行评论
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload2 = {"post_id": post_id,"content": "接口在"+date+"测试发布评论","is_post":"N"}
        member_id2 = "423"
        urlpart2 = '/comments/publish'
        result2 = self.r.interface_requests_data(member_id2, urlpart2, payload2)
        print('评论的comment_id：',result2['data']['comment_id'])

        payload = {'post_id': post_id, 'page': 1}
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------不存在的post----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 13
        print("testcase_002不存在的post:")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
