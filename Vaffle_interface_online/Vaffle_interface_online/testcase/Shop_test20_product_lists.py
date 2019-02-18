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

#---------------产品 - 产品列表----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------产品 - 产品列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 11
        row = 24
        member_id='68006'
        print ("testcase_001产品列表第一页数据:")

        payload={"shop_id":29388}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])

if __name__ == "__main__":
    unittest.main()