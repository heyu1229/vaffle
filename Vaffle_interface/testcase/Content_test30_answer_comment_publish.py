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

#---------------给回答评论----------------------
class AnswerCommentPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------给回答评论----------------------------------
    def testcase_001(self):
        i = 28120
        while i <= 28130:
            #从数据库取UUID
            i = i+1
            sql = SQL_vaffle ().select_uuid (i)
            uuid = '%s' % SQL_SEARCH_1 ().search ( sql )
            date = time.strftime ( "%Y-%m-%d %H:%M:%S", time.localtime () )
            url = Url().test_url()
            self.base_url1 =url + '/answer/comment/publish'
            headers = {"device": "android ", "version": "3.7.2", "lang": "en", "timestamp": "1564033489234",
                       "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                       "uuid": uuid, "Content-Type": "application/x-www-form-urlencoded",
                       "serial-number": "48525687125863258471123568955554", "company": "HUAWEI", "phone-model": "P10",
                       "system-version": "8.0.0"}
            payload = {"reply_id": "8641","content":"接口在" + date + "测试评论Q/A的回答","question_id":"8415"}
            result = requests.post ( self.base_url1, params=payload, headers=headers )
            result = result.json ()
            print(result)
            self.assertEqual ( 10000, result["code"] )
            print ( "code返回值：10000" )


if __name__ == "__main__":
    unittest.main()