# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc
import xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
#from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------群聊邀请向低版本用户发送升级消息----------------------
class Message(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------群聊邀请向低版本用户发送升级消息----------------------------------
    def testcase_001(self):
        sheet_index = 5
        row = 6
        print("testcase_001 群聊邀请向低版本用户发送升级消息：")
        member_id = "97f3fa2d-2aa7-484a-a811-3415873d0b0b"
        obj=({"q":"537abca4-4d62-4142-8728-75f36bc6c94f"})#537abca4-4d62-4142-8728-75f36bc6c94f bfe7b469-df07-4f45-9a35-3c743e1b76ae
        member_uuid=json.dumps(obj)
        payload={'member_uuid':member_uuid}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()