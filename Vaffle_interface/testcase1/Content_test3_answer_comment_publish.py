# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import json
import time

import xlrd

import global_list
from public_1.sql_search import SQL_SEARCH_1
from public_1.sql_vaffle import SQL_vaffle

sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------发布评论----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------批量给QA回答发布评论----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 11
        i = 37700
        print("testcase_001发布评论：")


        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()
        self.base_url1 =url + '/answer/comment/publish'
        while i <= 37700:
            #从数据库取UUID
            i = i+1
            sql = SQL_vaffle ().select_uuid (i)
            uuid = '%s' % SQL_SEARCH_1 ().search ( sql )
            print(uuid)
            payload = {"question_id": "42984","content": "接口在"+date+"1级评论用户ID"+str(i),"reply_id":"14883"}
            headers = {"device": "android ", "version": "3.7.0", "lang": "en", "timestamp": "1564033489234", "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                       "uuid": uuid,"serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"8.0.0"}
            result = requests.post(self.base_url1, params=payload, headers=headers)
            result = result.json()
            print(result)
        #global comment_id
        #comment_id = result["data"]["comment_id"]

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()