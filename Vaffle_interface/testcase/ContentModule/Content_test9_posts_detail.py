# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc,xlrd
import json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------动态详情----------------------
class PostsDetail(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------动态详情----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 15
        print("testcase_001动态详情：")

        # 调用发布接口发送一条动态，获取post_id
        member_id = "a0c77ee1-72e9-44a6-bb35-0c27291f8230"
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布post", "images": images, "category": "post"}
        # 获取发布接口token值
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        post_id = result1["data"]["post_id"]

        payload ={'post_id':post_id}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()