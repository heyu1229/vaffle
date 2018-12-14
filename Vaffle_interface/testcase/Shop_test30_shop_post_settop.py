# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------设置店铺置顶post数据----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------设置置顶----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 37
        member_id='10394'
        print ("testcase_001设置置顶:")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = { "content": "接口在" + date + "测试发布纯文字","normal_member_id":745}
        # 获取发布接口token值
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        print(result1)
        global post_id
        post_id = result1["data"]["post_id"]
        print("post_id=",post_id)

        payload={ "shop_id": 29388, "post_id":post_id, "state":1,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------取消置顶----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 38
        member_id='10394'
        print ("testcase_001取消置顶:")

        payload={ "shop_id": 29388, "post_id":post_id, "state":0, "normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
if __name__ == "__main__":
    unittest.main()