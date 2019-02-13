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

#---------------post点赞记录列表----------------------
class PostsDetail(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------动态编辑----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 58
        print("testcase_001动态编辑：")

        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布纯文字"}
        member_id = "744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        global post_id
        post_id = result1["data"]["post_id"]
        print("post_id=",post_id)

        # 2.调用动态编辑接口
        payload ={'post_id':post_id,'content':'接口在' + date + '编辑动态'}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # -----------------编辑别人的动态----------------------------------

    def testcase_002(self):
        sheet_index = 1
        row = 59
        print("testcase_002编辑别人的动态：")
        # 调用动态编辑接口
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {'post_id': post_id, 'content': '接口在' + date + '编辑动态'}
        member_id = "748"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10003, result["code"])
        print("code返回值：10003")

    #-----------------编辑review----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 100
        print("testcase_001动态编辑：")
        obj = ({"path":"https://s3-us-west-2.amazonaws.com/images-omv/posts/1532313355871_767_android.jpg","ratio":1.23,"tag":1},)
        images = json.dumps(obj)
        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content":"接口发布review content","category":"review","review_title":"接口在"+date+"发布review","review_product":"测评产品","review_type":"测评产品型号","publish_addr":"111"}
        member_id = "744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        global post_id
        post_id = result1["data"]["post_id"]

        # 2.调用动态编辑接口
        payload ={'post_id':post_id,'content':"接口在编辑review content","review_title":"接口在"+date+"编辑review","review_product":"测评产品","review_type":"测评产品型号"}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()