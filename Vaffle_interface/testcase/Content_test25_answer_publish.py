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
        # payload1 = { "content": "接口在" + date + "测试发布Q/A","category":"qa"}
        # member_id1 = "748"
        # urlpart = '/posts/publish'
        # result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)
        # print(result1)
        # global question_id
        # question_id = result1["data"]["question_id"]
        # print(question_id)

        obj=({"androidid":"1532313356301","imageUrl":"https://s3-us-west-2.amazonaws.com/images-omv/posts/1532313355871_767_android.jpg","radio":"1.0000","tag":1})
        aztec_images=json.dumps(obj)
        payload = {"question_id": "19183","content": "接口在" + date + "测试回答Q/A"}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        answer_id=result["data"]["answer_id"]
        print("answer_id=",answer_id)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        #回答成功后，删除回答，不然后面的接口不能再回答这个问题
        payload1 = { "answer_id": answer_id }
        member_id1 = "744"
        urlpart = '/answer/delete'
        result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)


if __name__ == "__main__":
    unittest.main()