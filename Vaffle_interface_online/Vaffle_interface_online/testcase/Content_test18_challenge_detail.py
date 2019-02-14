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
sys.path.append(global_list.path+"/log")
from interface_log import interface_log
from func_requests import FuncRequests

#---------------挑战详情----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------挑战详情---------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 25
        print ("testcase_001挑战详情:")

        # 调用/challenge/joinlist接口获取challenge_id
        payload1 = { "page": 1}
        member_id = "960"
        urlpart = '/challenge/joinlist'
        result1 = self.r.interface_requests_data(member_id, urlpart, payload1)
        list = result1["data"]["list"]
        challenge_id = list[0]["challenge_id"]
        print("challenge_id:", challenge_id)

        payload = {"page":1,"challenge_id":challenge_id}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()