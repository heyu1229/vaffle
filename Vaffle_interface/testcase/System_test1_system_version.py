744# -*- coding:UTF-8 -*-
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

#---------------新版本检测----------------------
class System_version(unittest.TestCase):

    def setUp(self):

        #路径
        self.url = Url().test_url()
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        self.base_url = self.obi.read_excel_data(3, 1, 4,self.filename)
        self.base_url1 = self.url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------新版本检测----------------------------------
    def testcase_001(self):
        url2 =self.url+"/interservice/version"
        r = requests.post ( url2)
        sheet_index = 3
        row = 1
        print("testcase_001新版本检测：")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        member_id = "744"
        token = Token().test_token1(payload, member_id)

        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        print(result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)

        if self.version =="2.2.0":
            self.assertEqual(10033, result["code"])
            print("code返回值：10033，No new version")
            self.obj.write_excel_data(sheet_index, row, 7, "No new version",self.path,self.filename)
        else :
            self.assertEqual(10000, result["code"])
            print("code返回值：10000")
            self.obj.write_excel_data(sheet_index, row, 7, "has new version",self.path,self.filename)


if __name__=="__main__":
    unittest.main()