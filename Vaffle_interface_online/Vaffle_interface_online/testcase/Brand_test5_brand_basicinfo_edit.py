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

#---------------修改品牌基本信息----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------修改品牌基本信息----------------------------------
    def testcase_001(self):
        sheet_index = 11
        row = 5
        member_id='34791'
        print ("testcase_001修改品牌基本信息:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"brand_id": 1, "brand_name": "brand_name" + date , "brand_intro": "brand_intro"+date, "brand_desc": "brand_desc" + date,
                   "ins_url": "ins_url" + date,"twitter_url": "twitter_url" + date,"youtube_url": "youtube_url" + date,
                   "email": "email" + date,"number": "number" + date,"address": "address" + date,"website": "website" + date,
                   "lon": "121" ,"lat": "31.5","logo":"avatar/1534491048212_1645_android.jpg","normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
