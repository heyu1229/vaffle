# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc
import json

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------举报用户----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

 # -----------------举报用户----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 24
        print("testcase_001举报用户：")
        s1 = "update vape_member_report_record set status=0 where report_member_id='746'"
        execute_sql1 = self.r.sql_vaffle(s1)
        member_id = "745"
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload={"report_member_id":746,"reason_id":1,"reason":"reason1","images":images}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

 # -----------------重复举报用户----------------------------------
    def testcase_002(self):
        sheet_index = 3
        row = 25
        print("testcase_002重复举报用户：")
        member_id = "745"
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload={"report_member_id":746,"reason_id":1,"reason":"reason1","images":images}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10130, result["code"])
        print("code返回值：10130")

if __name__=="__main__":
    unittest.main()