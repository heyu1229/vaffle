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

#---------------QA回答的评论列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------QA回答的评论列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 85
        print("testcase_001 QA回答的评论列表第一页数据：")

        # 调用发布接口发送一条QA，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # payload1 = { "content": "接口在" + date + "测试发布Q/A","category":"qa"}
        # member_id1 = "748"
        # urlpart = '/posts/publish'
        # result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)
        # print(result1)
        # global question_id
        # question_id = result1["data"]["question_id"]
        # print(question_id)

        # 调用QA回答接口发送一条回答，获得answer_id
        question_id="19183"
        payload2 = {"question_id": question_id, "content": "接口在" + date + "测试回答Q/A"}
        member_id2 = "744"
        urlpart2 = '/answer/publish'
        result2 = self.r.interface_requests_data(member_id2, urlpart2, payload2)
        global answer_id
        answer_id = result2["data"]["answer_id"]
        print("answer_id=",answer_id)

        # 调用评论QA回答接口发送一条评论
        payload3 = {"reply_id": answer_id, "content": "接口在" + date + "测试评论Q/A的回答","question_id":question_id}
        member_id3 = "744"
        urlpart3 = '/answer/comment/publish'
        result3 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result4 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result5 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result6 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result7 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result8 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result9 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result10 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result11= self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result12 = self.r.interface_requests_data(member_id3, urlpart3, payload3)
        result13 = self.r.interface_requests_data(member_id3, urlpart3, payload3)

        print(result3["data"]["comment_id"],result4["data"]["comment_id"],result5["data"]["comment_id"],result6["data"]["comment_id"],result7["data"]["comment_id"],result8["data"]["comment_id"],result9["data"]["comment_id"],result10["data"]["comment_id"],result11["data"]["comment_id"],result12["data"]["comment_id"],result13["data"]["comment_id"])
        obj=(result3["data"]["comment_id"],result4["data"]["comment_id"],result5["data"]["comment_id"],result6["data"]["comment_id"],result7["data"]["comment_id"],result8["data"]["comment_id"],result9["data"]["comment_id"],result10["data"]["comment_id"],result11["data"]["comment_id"],result12["data"]["comment_id"])
        global comment_id_past,comment_id
        comment_id_past=json.dumps(obj)
        comment_id=result3["data"]["comment_id"]
        print("comment_id=",comment_id)
        payload = {"answer_id": answer_id,"page": 1}
        member_id="744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------用户对于Q／A的回答列表第二页数据-----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 86
        print("testcase_002 用户对于Q／A的回答列表二页数据：")
        member_id = "744"
        payload = {"answer_id": answer_id, "page": 2, "comment_id_past": comment_id_past}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------评论置顶-----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 101
        print("testcase_003 评论置顶：")
        member_id = "744"
        payload = {"answer_id": answer_id, "page": 1, "comment_id": comment_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # 回答成功后，删除回答，不然后面的接口不能再回答这个问题
        payload1 = {"answer_id": answer_id}
        member_id1 = "744"
        urlpart = '/answer/delete'
        result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)

if __name__ == "__main__":
    unittest.main()