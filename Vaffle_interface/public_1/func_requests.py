#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc
import json
import xlrd
import pymysql.cursors
#from get_token import Token
from Vaffle_interface.public_1.get_url import Url
from Vaffle_interface.public_1.read_data import Read_ExcelData
from Vaffle_interface.public_1.write_data import Write_ExcelData
from Vaffle_interface.public_1.get_version import Version
#---------------关注----------------------



class FuncRequests():

    #-----------------接口请求（payload从文件中读取,且调用read_excel_data_dict方法）----------------------------------
    def interface_requests(self,member_id,sheet_index,row):
        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        print("url:", self.base_url1)
        # 获取版本
        self.version = Version().test_version()
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5)
        #获取token值
        #token = Token().test_token1(payload, member_id)
        token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

        #记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "uuid": member_id,"serial-number":"48525687125863258471123568955554","company":"HUAWEI",
                   "phone-model":"P10","system-version":"system_version",'Content-Type':'application/x-www-form-urlencoded'}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, ensure_ascii=False, indent=1)
        print(headers)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:65535],self.path)
            self.obj.write_excel_data ( sheet_index, row, 10, str_result[65536:131071], self.path )
            self.obj.write_excel_data ( sheet_index, row, 11, str_result[131072:], self.path )
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path)
        return result

    # -----------------接口请求（payload动态获取）----------------------------------
    def interface_requests_payload(self,member_id,sheet_index,row,payload):

        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        print("url:", self.base_url1)
        # 获取版本
        self.version = Version().test_version()
        payload = payload
        #获取token值
        #token = Token().test_token1(payload, member_id)
        token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

        # 记录接口的请求时间
        start = time.time()
        headers = {"device": "android", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "uuid": member_id,"serial-number":"48525687125863258471123568955554","company":"HUAWEI",
                   "phone-model":"P10","system-version":"system_version",'Content-Type':'application/x-www-form-urlencoded'}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, ensure_ascii=False, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:65535],self.path)
            self.obj.write_excel_data ( sheet_index, row, 10, str_result[65536:131071], self.path )
            self.obj.write_excel_data ( sheet_index, row, 11, str_result[131072:], self.path )
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path)
        return result


    #-----------------接口请求（payload从文件中读取,且调用read_excel_data方法）----------------------------------
    def interface_requests2(self,member_id,sheet_index,row):
        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version().test_version()
        payload = self.obi.read_excel_data(sheet_index, row, 5)
        #获取token值
        #token = Token().test_token1(payload, member_id)
        token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

        #记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "uuid": member_id,"serial-number":"48525687125863258471123568955554","company":"HUAWEI",
                   "phone-model":"P10","system-version":"system_version",'Content-Type':'application/x-www-form-urlencoded'}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, ensure_ascii=False,indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:65535],self.path)
            self.obj.write_excel_data ( sheet_index, row, 10, str_result[65536:131071], self.path )
            self.obj.write_excel_data ( sheet_index, row, 11, str_result[131072:], self.path )
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path)
        return result


    # -----------------调用其他接口动态获得要使用的字段----------------------------------
    def interface_requests_data(self,member_id,urlpart,payload):
        # 获取EXcel路径
        self.path = Url().test_path()
        # 路径
        url = Url().test_url()
        print()
        self.base_url=url+urlpart
        self.obi = Read_ExcelData()
        # 获取版本
        self.version = Version().test_version()
        #获取token值
        #token = Token().test_token1(payload, member_id)
        token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "uuid": member_id,"serial-number":"48525687125863258471123568955554","company":"HUAWEI",
                   "phone-model":"P10","system-version":"system_version",'Content-Type':'application/x-www-form-urlencoded'}
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        return result

    def sql_vaffle(self,s):
        # 连接MySQL数据库
        connection = pymysql.connect(host='172.100.200.62', port=3306, user='root', password='heavengifts',
                                     db='vaffle',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


        # 通过cursor创建游标
        cursor = connection.cursor()

        # 创建sql 语句，并执行
        sql = s
        cursor.execute(sql)

        # 提交SQL
        connection.commit()

    def sql_vaffle_post(self,s):
        # 连接MySQL数据库
        connection = pymysql.connect(host='172.100.200.62', port=3306, user='root', password='heavengifts',
                                     db='vaffle_post',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


        # 通过cursor创建游标
        cursor = connection.cursor()

        # 创建sql 语句，并执行
        sql = s
        execute=cursor.execute(sql)
        results=cursor.fetchall()
        for result in results:
            if result == None:
                return None
            else:
                return result
        # 提交SQL
        connection.commit()

   #-----------------接口请求（payload从文件中读取,且调用read_excel_data_dict方法）----------------------------------
    def interface_requests_apitest2(self,member_id,sheet_index,row):
        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url1()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        # 获取版本
        self.version = Version().test_version()
        payload = self.obi.read_excel_data_dict(sheet_index, row, 5)
        #获取token值
        #token = Token().test_token1(payload, member_id)
        token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

        #记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "uuid": member_id,"serial-number":"48525687125863258471123568955554","company":"HUAWEI",
                   "phone-model":"P10","system-version":"system_version",'Content-Type':'application/x-www-form-urlencoded'}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, ensure_ascii=False, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:65535],self.path)
            self.obj.write_excel_data ( sheet_index, row, 10, str_result[65536:131071], self.path )
            self.obj.write_excel_data ( sheet_index, row, 11, str_result[131072:], self.path )
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path)
        return result

    # -----------------接口请求（payload动态获取）----------------------------------
    def interface_requests_payload_apitest2(self,member_id,sheet_index,row,payload):

        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url1()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        print(self.base_url1)
        # 获取版本
        self.version = Version().test_version()
        payload = payload
        #获取token值
        #token = Token().test_token1(payload, member_id)
        token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

        # 记录接口的请求时间
        start = time.time()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "uuid": member_id,"serial-number":"485256871258632584711235689555542","company":"HUAWEI",
                   "phone-model":"P10","system-version":"system_version",'Content-Type':'application/x-www-form-urlencoded'}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, ensure_ascii=False, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:65535],self.path)
            self.obj.write_excel_data ( sheet_index, row, 10, str_result[65536:131071], self.path )
            self.obj.write_excel_data ( sheet_index, row, 11, str_result[131072:], self.path )
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path)
        return result


    # -----------------接口请求（header中要传tik）----------------------------------
    def interface_requests_payload_tik(self,member_id,sheet_index,row,payload,tik):

        # 获取EXcel路径
        self.path = Url().test_path()

        # 路径
        url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(sheet_index, row, 4)
        self.base_url1 = url + self.base_url
        print("url:", self.base_url1)
        # 获取版本
        self.version = Version().test_version()
        payload = payload
        #获取token值
        #token = Token().test_token1(payload, member_id)
        token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

        # 记录接口的请求时间
        start = time.time()
        headers = {"tik":tik,"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token,
                   "uuid": member_id,"serial-number":"48525687125863258471123568955554","company":"HUAWEI",
                   "phone-model":"P10","system-version":"system_version",'Content-Type':'application/x-www-form-urlencoded'}
        r = requests.post(self.base_url1, params=payload, headers=headers)
        result = r.json()
        format_result = json.dumps(result, ensure_ascii=False, indent=1)
        print(format_result)
        end = time.time()

        # 写入excel中
        str_result = str(result)
        self.obj = Write_ExcelData()
        self.obj.write_excel_data(sheet_index, row, 6, result["code"],self.path)
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:65535],self.path)
            self.obj.write_excel_data ( sheet_index, row, 10, str_result[65536:131071], self.path )
            self.obj.write_excel_data ( sheet_index, row, 11, str_result[131072:], self.path )
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path)
        self.obj.write_excel_data(sheet_index, row, 10, end - start,self.path)
        return result