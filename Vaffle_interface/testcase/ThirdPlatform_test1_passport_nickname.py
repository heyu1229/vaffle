# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#---------------检测第三方是否注册----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):

        #路径
        url = Url().test_url()
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        self.base_url = self.obi.read_excel_data(6, 1, 4,self.filename)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------	检测第三方已注册----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 1
        print("testcase_001检测第三方已注册：")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        token = Token().test_token(payload)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": "none"}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result=r.json()
        data=result["data"]
        print(result)
        end = time.time ()
        # 写入excel中
        self.obj.write_excel_data ( sheet_index, row, 10, end - start ,self.path,self.filename)
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        self.assertEqual(1, len(data["list"]))
        print("推荐的用户昵称等于1，表示已经注册")
        self.obj.write_excel_data(sheet_index, row, 7, "推荐的用户昵称等于1，表示已经注册",self.path,self.filename)


    #-----------------	检测第三方未注册----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_002(self):
        sheet_index = 6
        row = 2
        print("testcase_001检测第三方未注册：")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        token = Token().test_token(payload)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": "none"}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result=r.json()
        data=result["data"]
        print(result)
        end = time.time ()
        # 写入excel中
        self.obj.write_excel_data ( sheet_index, row, 10, end - start,self.path,self.filename )
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.assertEqual(5, len(data["list"]))
        print("推荐的用户昵称不等于1，表示未注册")
        self.obj.write_excel_data(sheet_index, row, 7, "推荐的用户昵称不等于1，表示未注册",self.path,self.filename)



if __name__=="__main__":
    unittest.main()
