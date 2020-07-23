# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc
import xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------与用户相关的QA信息列表----------------------
class Message(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------QA消息列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 5
        row =3
        print("testcase_001QA消息列表第一页数据：")
        member_id1 = "748"
        result=self.r.interface_requests(member_id1,sheet_index,row)
        message_list = result['data']['list']
        global question_id,comment_id,member_id,category
        question_id = message_list[9]['question_id']
        comment_id = message_list[9]['comment_id']
        member_id = message_list[9]['member_id']
        category = message_list[9]['category']
        print(question_id, comment_id, member_id, category)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------QA消息列表第二页数据----------------------------------
    def testcase_002(self):
        sheet_index = 5
        row =4
        print("testcase_002 QA消息列表第二页数据：")
        member_id1 = "748"
        payload = {"page":2,"question_id":question_id,"comment_id":comment_id,"member_id":member_id,"category":category}
        result = self.r.interface_requests_payload(member_id1, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()