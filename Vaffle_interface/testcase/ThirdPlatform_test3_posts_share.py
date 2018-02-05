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
#---------------第三方分享回调接口----------------------
class Post_share(unittest.TestCase):

    def setUp(self):

        #路径
        self.url = Url().test_url()
        # 获取EXcel路径
        self.path = Url ().test_path ()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        self.base_url = self.obi.read_excel_data(6, 7, 4,self.filename)
        self.base_url1 = self.url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------第三方分享回调----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 7
        print("testcase_001第三方分享回调")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布纯文字"}
        # 获取发布接口token值
        member_id = "744"
        token1 = Token().test_token1(payload1, member_id)

        headers1 = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505",
                    "token": token1,
                    "login": member_id}
        r1 = requests.post(self.url + "/posts/publish", params=payload1, headers=headers1)
        result1 = r1.json()
        post_id = result1["data"]["post_id"]
        print(post_id)

        payload = {'platform':'facebook','post_id':post_id}
        # 获取token值
        member_id = "744"
        token = Token().test_token1(payload, member_id)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result=r.json()
        print(result)
        end = time.time ()
        # 写入excel中
        self.obj.write_excel_data ( sheet_index, row, 10, end - start ,self.path,self.filename)
        str_result = str(result)
        Write_ExcelData().write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        Write_ExcelData().write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            Write_ExcelData().write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            Write_ExcelData().write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            Write_ExcelData().write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        self.assertEqual("ok", result["msg"])
        print("msg返回值：ok")


    #-----------------不支持的第三方----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_002(self):
        sheet_index = 6
        row = 8
        print("testcase_002不支持的第三方")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        member_id = "744"
        token = Token().test_token1(payload, member_id)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result=r.json()
        print(result)
        end = time.time ()
        # 写入excel中
        self.obj.write_excel_data ( sheet_index, row, 10, end - start ,self.path,self.filename)
        str_result = str(result)
        Write_ExcelData().write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        Write_ExcelData().write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            Write_ExcelData().write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            Write_ExcelData().write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            Write_ExcelData().write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(9999, result["code"])
        print("code返回值：9999")
        self.assertEqual("Time out.", result["msg"])
        print("msg返回值：Time out.")


    #-----------------分享app----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_003(self):
        sheet_index = 6
        row = 9
        print("testcase_003分享app：")
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        # 获取token值
        member_id = "744"
        token = Token().test_token1(payload, member_id)
        start = time.time ()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id}
        r = requests.post(self.base_url1,params=payload,headers=headers)
        result=r.json()
        print(result)
        end = time.time ()
        # 写入excel中
        self.obj.write_excel_data ( sheet_index, row, 10, end - start ,self.path,self.filename)
        str_result = str(result)
        Write_ExcelData().write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        Write_ExcelData().write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            Write_ExcelData().write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            Write_ExcelData().write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            Write_ExcelData().write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()
