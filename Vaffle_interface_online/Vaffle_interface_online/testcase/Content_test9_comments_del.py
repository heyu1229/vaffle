# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import json
import time,xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------评论删除功能----------------------
class CommentsDel(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------删除自己的评论----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 13
        print("testcase_001删除评论：")

        # 1.调用评论接口，获得comment_id
        member_id = "960"
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload2 = {"post_id": 6523, "content": "haha", "is_post": "N"}
        urlpart2 = '/comments/publish'
        result2 = self.r.interface_requests_data(member_id, urlpart2, payload2)
        comment_id = result2["data"]["comment_id"]
        print(comment_id)

        # 获取删除评论接口的token值
        payload =  {"comment_id": comment_id}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()

