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
#from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
sys.path.append(global_list.path+"/log")
from interface_log import interface_log
from func_requests import FuncRequests

#---------------发送邀请----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------发送邀请---------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 10

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 发送邀请:")

        payload={"guid":"3bd8c58a-49fb-4ea1-bbdb-0a00c12d6f90"}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])

if __name__ == "__main__":
    unittest.main()