#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc
import json
import xlrd
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#---------------关注----------------------
class FuncRequests():

    #-----------------接口请求（payload从文件中读取）----------------------------------
    def interface_requests(self,member_id,sheet_index,row):

        # 获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = xlrd.open_workbook(self.path)

        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4, self.filename)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version().test_version()
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5,self.filename)
        #获取token值
        token = Token().test_token1(payload, member_id)

        #记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id,"serial_number":"48525687125863258471123568955554","company":"HUAWEI","phone_model":"P10","system_version":"system_version"}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        return result

    # -----------------接口请求（payload动态获取）----------------------------------
    def interface_requests_payload(self,member_id,sheet_index,row,payload):

        # 获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = xlrd.open_workbook(self.path)
        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4, self.filename)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version().test_version()
        payload = payload
        #获取token值
        token = Token().test_token1(payload, member_id)

        # 记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "login": member_id,"serial_number":"48525687125863258471123568955554","company":"HUAWEI","phone_model":"P10","system_version":"system_version"}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path,self.filename)
        return result
