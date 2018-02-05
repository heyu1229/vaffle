# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc,xlrd
import time
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#---------------转发----------------------
class PostsRepeat(unittest.TestCase):

    def setUp(self):
        # 获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        #路径
        self.url = Url().test_url()
        self.obi = Read_ExcelData()
        self.base_url = self.obi.read_excel_data(1, 19, 4,self.filename)
        self.base_url1 = self.url + self.base_url
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()

    #-----------------转发----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 19
        print("testcase_001转发：")

        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"uid": "744", "content": "接口在" + date + "测试发布纯文字"}
        # 获取发布接口token值
        member_id = "744"
        token1 = Token().test_token1(payload1, member_id)

        headers1 = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": token1,
                    "login": member_id}
        r1 = requests.post(self.url+"/posts/publish", params=payload1, headers=headers1)
        result1 = r1.json()
        global post_id
        post_id = result1["data"]["post_id"]

        payload = {"uid": "744","post_id": post_id,"content": "接口在"+date+"转发测试"}
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


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)

    # -----------------转发时content为空----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 41
        print("testcase_002转发时content为空：")
        payload = {"uid": "744", "post_id": post_id}
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


        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        self.obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)

    #-----------------转发postid不存在----------------------------------
    def testcase_003(self):
        sheet_index = 1
        row = 42
        print("testcase_003转发post_id不存在：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"uid": "744","post_id": "99999999","content": "接口在"+date+"转发测试"}
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
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10003, result["code"])
        print("code返回值：10003")
        self.assertEqual("Parameter Error", result["msg"])
        print("msg返回值：Parameter Error")

    #-----------------转发uid不存在----------------------------------
    def testcase_004(self):
        sheet_index = 1
        row = 43
        print("testcase_004转发uid不存在：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"post_id": post_id,"content": "接口在"+date+"转发测试"}
        # 获取token值
        member_id = "9999999"
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
        self.obj.write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)
        if len(str_result) > 32767:
            self.obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            self.obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            self.obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)


        self.assertEqual(10040, result["code"])
        print("code返回值：10040")

        self.assertEqual("This user does not exist.", result["msg"])
        print("msg返回值：This user does not exist.")


if __name__=="__main__":
    unittest.main()