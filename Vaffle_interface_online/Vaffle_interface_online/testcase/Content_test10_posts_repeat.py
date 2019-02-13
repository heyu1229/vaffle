# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc,xlrd
import time
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------转发----------------------
class PostsRepeat(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------转发----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 19
        print("testcase_001转发：")

        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"uid": "744", "content": "接口在" + date + "测试发布纯文字"}
        member_id = "744"
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        print(result1)
        global post_id
        post_id = result1["data"]["post_id"]

        payload = {"uid": "744","post_id": post_id,"content": "接口在"+date+"转发测试"}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------转发时content为空----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 41
        print("testcase_002转发时content为空：")
        payload = {"uid": "744", "post_id": post_id}
        # 获取token值
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------转发postid不存在----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 42
        print("testcase_003转发post_id不存在：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"uid": "744","post_id": "99999999","content": "接口在"+date+"转发测试"}
        # 获取token值
        member_id = "744"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10003, result["code"])
        print("code返回值：10003")

    #-----------------转发uid不存在----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 43
        print("testcase_004转发uid不存在：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"post_id": post_id,"content": "接口在"+date+"转发测试"}
        # 获取token值
        member_id = "9999999"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10040, result["code"])
        print("code返回值：10040")

if __name__=="__main__":
    unittest.main()