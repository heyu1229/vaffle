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

#---------------申请成为店铺店主----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------申请成为店铺店主----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 27
        member_id='746'
        print ("testcase_001申请成为店铺店主:")

        payload = {"name": "接口测试店铺", "nation": "china","city": "shangai","address": "qilianshanlu",
                   "first_name": "first_name","last_name": "last_name","img_card_front":"posts/1512710644871_767_android.jpg",
                   "img_card_back":"posts/1512710644871_767_android.jpg","img_license":"posts/1512710644871_767_android.jpg"}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()