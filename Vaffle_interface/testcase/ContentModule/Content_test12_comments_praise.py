# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import json
import time,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------评论点赞/取消点赞----------------------

class CommentsDel(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------评论点赞----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 18
        print("testcase_001评论点赞：")

        #1.调用发布接口发送一条动态，获取post_id
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布post", "images": images, "category": "post"}
        # 获取发布接口token值
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        post_id = result1["data"]["post_id"]

        # 2.调用评论接口，获得comment_id
        urlpart2 = '/comments/publish'
        payload2 = {'post_id': post_id, "content": "接口测试发布评论" + date}
        result2 = self.r.interface_requests_data(member_id, urlpart2, payload2)
        global comment_id
        comment_id = result2["data"]["comment_id"]
        print(comment_id)

        payload =  {"comment_id": comment_id,"praise_state":1}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------评论取消点赞----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 19
        print("testcase_002 评论取消点赞：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload =  {"comment_id": comment_id,"praise_state":0}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()