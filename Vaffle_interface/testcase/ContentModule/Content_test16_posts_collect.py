# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc,xlrd
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------动态收藏/取消收藏----------------------
class CommentsLists(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------动态收藏----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 23
        print("testcase_001评论列表:")

        # 1.调用发布接口发送一条动态，获取post_id
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布post", "images": images, "category": "post"}
        # 获取发布接口token值
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        global post_id
        post_id = result1["data"]["post_id"]
        print(post_id)

        #2.调用动态收藏/取消收藏接口
        payload = {'post_id': post_id, 'state': 1}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------取消收藏----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 24
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload = {'post_id': post_id, 'state': 0}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
