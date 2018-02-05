# -*- coding:UTF-8 -*-
import unittest
import requests,gc
import sys,time

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#---------------第三方登录接口----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):

        #路径
        url = Url().test_url()
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        self.base_url = self.obi.read_excel_data(6, 3, 4,self.filename)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------第三方facebook登录成功----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 3
        print("testcase_001第三方facebook登录成功：")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        member_id = "744"
        token = Token().test_token(payload)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": "none"}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result=r.json()
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
        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


     # -----------------第三方twitter登录成功----------------------------------
    # -----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------

    def testcase_002(self):
        sheet_index = 6
        row = 4
        print("testcase_002第三方twitter登录成功：")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        member_id = "744"
        token = Token().test_token(payload)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": "none"}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
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
        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


    # -----------------第三方vk登录成功----------------------------------
    # -----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_003(self):
        sheet_index = 6
        row = 5
        print("testcase_003第三方vk登录成功：")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        member_id = "744"
        token = Token().test_token(payload)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": "none"}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
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
        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)


        # -----------------不支持的第三方--------------------------
    def testcase_004(self):
        sheet_index = 6
        row = 6
        print("testcase_004不支持的第三方：")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        member_id = "744"
        token = Token().test_token(payload)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": "none"}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        print(result)
        end = time.time ()
        # 写入excel中
        self.obj.write_excel_data ( sheet_index, row, 10, end - start ,self.path,self.filename)
        str_result = str(result)
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(9999, result["code"])
        print("code返回值：9999")

        self.assertEqual("Time out.", result["msg"])
        print("msg返回值：Time out.")

    # -----------------第三方INS登录成功----------------------------------
    def testcase_005(self):
        sheet_index = 6
        row = 10
        print ( "testcase_003第三方ins登录成功：" )
        payload = Read_ExcelData ().read_excel_data_dict ( sheet_index, row, 5, self.filename )
        # 获取token值
        member_id = "744"
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                   "token": token,
                   "login": "none"}
        r = requests.post ( self.base_url1, params=payload, headers=headers )
        result = r.json ()
        print ( result )
        end = time.time ()
        # 写入excel中
        self.obj.write_excel_data ( sheet_index, row, 10, end - start, self.path, self.filename )
        str_result = str ( result )
        self.obj.write_excel_data ( sheet_index, row, 6, result["code"], self.path, self.filename )
        if len ( str_result ) > 32767:
            self.obj.write_excel_data ( sheet_index, row, 8, str_result[0:32767], self.path, self.filename )
            self.obj.write_excel_data ( sheet_index, row, 9, str_result[32767:], self.path, self.filename )
        else:
            self.obj.write_excel_data ( sheet_index, row, 8, str_result, self.path, self.filename )

        self.assertEqual ( 10000, result["code"] )
        print ( "code返回值：10000" )
        self.assertEqual ( "", result["msg"] )
        print ( "msg返回值：ok" )
        self.obj.write_excel_data ( sheet_index, row, 7, "ok", self.path, self.filename )

if __name__=="__main__":
    unittest.main()
