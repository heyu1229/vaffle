# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import json
import time

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------发表Q/A的回答----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------发表Q/A的回答----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 71
        print("testcase_001 发表Q/A的回答：")

        # 调用发布接口发送一条动态，获取question_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = { "content": "接口在" + date + "测试发布Q/A","category":"qa"}
        member_id1 = "748"
        urlpart = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)
        print(result1)
        global question_id
        question_id = result1["data"]["question_id"]
        print(question_id)

        obj=({"androidid":"1532313356301","imageUrl":"https://s3-us-west-2.amazonaws.com/images-omv/posts/1532313355871_767_android.jpg","radio":"1.0000","tag":1})
        aztec_images=json.dumps(obj)
        payload = {"question_id": question_id,"content": "接口在" + date + "测试回答Q/A\u97ed\u83dc\u9e21\u86cb\u5c31<b>\u56de\u5230\u5bb6</b>\u000a\u000a<cite><strong>\u597d\u7684</strong></cite>\u000a\u000a<hr>\u000a\u000a<cite><strong></strong></cite><cite><strong></strong></cite>\u000a\u000a<img src='https://s3-us-west-2.amazonaws.com/images-omv/posts/1532312552416_980_android.jpg' androidid='1532339624238' width='984' height='984'>\u000a\u000a<!--more&lt;cite&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/cite&gt;-->"}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()