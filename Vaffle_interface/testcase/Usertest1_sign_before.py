# -*- coding:UTF-8 -*-
import json
import unittest
import requests,gc
import sys

import time
import global_list
sys.path.append(global_list.path+"/public_1")
import xlrd
from get_token import Token
from get_url import Url
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version

#---------------用户注册第一阶段返回nickname----------------------

class SignBefore(unittest.TestCase):

    def setUp(self):
        #路径
        self.url = Url().test_url()
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------用户注册成功，list返回5个nickname----------------------------------
    def testcase_001(self):

        #获取路径
        url1 = self.obi.read_excel_data ( 0, 1, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 1, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        #obj = Write_ExcelData ()
        self.obj.write_excel_data( 0, 1, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 1, 7, result['msg'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 1, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 1, 9, end - start,self.path,self.filename)


        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")




    #-----------------邮箱账号已被注册----------------------------------
    def testcase_002(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 2, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 2, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 2, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 2, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 2, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 2, 9, end - start,self.path,self.filename )

        self.assertEqual(10002, result['code'])
        print("code返回值：10002")
        self.assertEqual('The email address has been taken.', result['msg'])
        print("msg返回值：The email address has been taken.")


    #-----------------邮箱账号格式错误----------------------------------
    def testcase_003(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 3, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 3, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 3, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 3, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 3, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 3, 9, end - start ,self.path,self.filename)

        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")




    #-----------------密码不足6位----------------------------------
    def testcase_004(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 4, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 4, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 4, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 4, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 4, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 4, 9, end - start ,self.path,self.filename)


        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")


    #-----------------密码超过20位----------------------------------
    def testcase_005(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 5, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 5, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 5, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 5, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 5, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 5, 9, end - start ,self.path,self.filename)


        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

    #-----------------密码纯数字----------------------------------
    def testcase_006(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 6, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 6, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 6, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 6, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 6, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 6, 9, end - start,self.path,self.filename )

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


    #-----------------密码纯字母----------------------------------
    def testcase_007(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 7, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0,7, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 7, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 7, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 7, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 7, 9, end - start,self.path,self.filename )


        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


    #----------------displayname为空----------------------------------
    def testcase_008(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 8, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0,8, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 8, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 8, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 8, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 8, 9, end - start ,self.path,self.filename)

        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")


    #-----------------displayname少于3位----------------------------------
    def testcase_009(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 9, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 9, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 9, 6, result['code'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 9, 7, result['msg'] ,self.path,self.filename )
        self.obj.write_excel_data ( 0, 9, 8, str(result) ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 9, 9, end - start ,self.path,self.filename)


        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

    #-----------------displayname超过30位----------------------------------
    def testcase_010(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 10, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 10, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version':self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 10, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 10, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 10, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 10, 9, end - start,self.path,self.filename )


        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

    # -----------------displayname含特殊字符校验通过----------------------------------
    def testcase_011(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 11, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        start = time.time ()
        payload =self.obi.read_excel_data_dict ( 0, 11, 5,self.filename)
        token = Token ().test_token ( payload )
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 11, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 11, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 11, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 11, 9, end - start,self.path,self.filename )

        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )


        gc.collect()
if __name__ == '__main__':
    unittest.main ()
