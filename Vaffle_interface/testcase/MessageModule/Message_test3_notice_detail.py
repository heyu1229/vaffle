'''
------------------此接口已不存在----------------
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc
import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#---------------通知详情----------------------------
class MessageceDel(unittest.TestCase):

    def setUp(self):
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        #路径
        url = Url().test_url()
        self.base_url = self.obi.read_excel_data(5, 3, 4,self.filename)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()


    #-----------------通知详情----------------------------------
    def testcase_001(self):
        sheet_index = 5
        row = 3
        print("testcase_001删除与某人的对话：")
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
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)

        try:
            self.assertEqual(10000, result["code"])
            print("code返回值：10000")
        except AssertionError as e:
            print("code返回值：非10000，", result["code"])

        try:
            self.assertEqual("", result["msg"])
            print("msg返回值：ok")
            self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)
        except AssertionError as e:
            print("msg返回报错：", result["msg"])
            self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        gc.collect()
if __name__=="__main__":
    unittest.main()

'''