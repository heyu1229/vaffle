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

#---------------（品牌）话题详情----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------话题详情----------------------------------

    def testcase_001(self):
        sheet_index = 11
        row = 14
        print ("testcase_001话题详情:")

        # 调用话题发布，获取topic_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"brand_id": 1,"title":"接口发布的话题"+date,"topic_content":"用来被删除"}
        member_id1 = "744"
        urlpart1 = '/brandtopic/public'
        result1 = self.r.interface_requests_data(member_id1, urlpart1, payload1)
        print(result1)
        topic_id = result1["data"]["brand_topic_id"]
        print("topic_id=",topic_id)

        member_id = '777'
        payload = {"topic_id": topic_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
