# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc,xlrd,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------举报动态----------------------
class PostsReport(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------举报动态----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 13
        print("testcase_001举报动态：")

        # 调用发布接口发送一条动态，获取post_id
        member_id = "a0c77ee1-72e9-44a6-bb35-0c27291f8230"
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布post用于举报", "images": images, "category": "post"}
        # 获取发布接口token值
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        print(result1)
        post_id = result1["data"]["post_id"]

        payload ={"post_id": post_id,"reason_id":"21","type":1}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()