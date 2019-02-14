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

#---------------动态详情----------------------
class PostsDetail(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------动态详情----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 12
        print("testcase_001动态详情：")

        # 调用posts/lists接口获取post_id
        payload1 = {"type": "post", "page": 1}
        member_id1 = "960"
        urlpart = '/posts/lists'
        result1 = self.r.interface_requests_data(member_id1, urlpart, payload1)
        list = result1["data"]["list"]
        post_id = list[0]["post_id"]
        print("post_id:",post_id)

        payload ={'post_id':post_id}

        member_id = "960"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()