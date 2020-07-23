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

#---------------更新群组信息----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------更新群组信息title必填验证---------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 4
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 更新群组信息title必填验证:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"guid":"df698e1f-2d38-4ff6-8335-394f715dc437","title":""}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------更新群组信息guid必填验证---------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 4
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_002 更新群组信息guid必填验证:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"guid":"","title":"xtitle"+date}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------更新群组信息---------------------------
    def testcase_003(self):
        sheet_index = 14
        row = 4
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_003 更新群组信息:")

        obj = ({"facebook":"testfacebook","vk":"vktests"},)
        media = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"guid":"df698e1f-2d38-4ff6-8335-394f715dc437","title":"xtitle"+date,"group_description":"xgroup_description",
                   "email":"7898329@qq.com","website":"www.baidu1.com","address":"addresstest","media":media}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()