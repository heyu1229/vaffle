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
#-----------------------用户注册最后阶段接口---------------------------
class SignUp(unittest.TestCase):

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
    #-----------------注册成功----------------------------------
    def testcase_001(self):
        print("注册成功：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 12, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        nickname = 'heyu'+nowTime
        email = 'heyu'+nowTime+'@qq.com'
        print(email)
        payload = {'email': email,'password': 'aaa111','displayname': 'heyu','nickname': nickname,'equipment_number': 'PE-TL10',}
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 12, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 12, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 12, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 12, 9, end - start ,self.path,self.filename)


        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    #-----------------nickname已存在----------------------------------
    def testcase_002(self):
        print("nickname已存在：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 13, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 13, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 13, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 13, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 13, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 13, 9, end - start ,self.path,self.filename)


        self.assertEqual(10044, result['code'])
        print("code返回值：10044")

        self.assertEqual('This name is occupied. Please try another one.', result['msg'])
        print("msg返回值：This name is occupied. Please try another one.")

    # -----------------nickname为空----------------------------------
    def testcase_003(self):
        print("nickname为空：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 14, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 14, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 14, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 14, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 14, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 14, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------nickname少于3位----------------------------------
    def testcase_004(self):
        print("nickname少于3位：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 15, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 15, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 15, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 15, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 15, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 15, 9, end - start,self.path,self.filename )

        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The nickname should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The nickname should be 3-30 characters (letters, digits or underline)" )

    # -----------------nickname超过30位----------------------------------
    def testcase_005(self):
        print("nickname超过30位：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 16, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 16, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 16, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 16, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 16, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 16, 9, end - start ,self.path,self.filename)

        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The nickname should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The nickname should be 3-30 characters (letters, digits or underline)" )

    # -----------------nickname字符前有空格报错----------------------------------
    def testcase_006(self):
        print("nickname字符前有空格报错：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 17, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 17, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 17, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 17, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 17, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 17, 9, end - start,self.path,self.filename )

        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The nickname should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The nickname should be 3-30 characters (letters, digits or underline)" )

    # -----------------nickname字符间有空格报错----------------------------------
    def testcase_007(self):
        print("nickname字符间有空格报错：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 18, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 18, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 18, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 18, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 18, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 18, 9, end - start,self.path,self.filename )


        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The nickname should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The nickname should be 3-30 characters (letters, digits or underline)" )

    # -----------------nickname含特殊字符报错----------------------------------
    def testcase_008(self):
        print("nickname含特殊字符报错：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 19, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 19, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version':self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 19, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 19, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 19, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 19, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 10045, result['code'] )
        print ( "code返回值：10045" )
        self.assertEqual ( 'The nickname should be 3-30 characters (letters, digits or underline)', result['msg'] )
        print ( "msg返回值：The nickname should be 3-30 characters (letters, digits or underline)" )

    # -----------------邮箱账号已被注册----------------------------------
    def testcase_009(self):
        print("邮箱账号已被注册：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 20, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 20, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 20, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 20, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 20, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 20, 9, end - start ,self.path,self.filename)

        self.assertEqual ( 10002, result['code'] )
        print ( "code返回值：10002" )

        self.assertEqual ( 'The email address has been taken.', result['msg'] )
        print ( "msg返回值：The email address has been taken." )

    # -----------------邮箱账号格式错误----------------------------------
    def testcase_010(self):
        print("邮箱账号格式错误：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 21, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 21, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 21, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 21, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 21, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 21, 9, end - start,self.path,self.filename )

        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------密码不足6位----------------------------------
    def testcase_011(self):
        print("密码不足6位：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 22, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 22, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 22, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 22, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 22, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 22, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )

        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------密码超过20位----------------------------------
    def testcase_012(self):
        print("密码超过20位：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 23, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 23, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 23, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 23, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 23, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 23, 9, end - start ,self.path,self.filename)

        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )

        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------密码不限特殊字符----------------------------------
    def testcase_013(self):
        print("密码不限特殊字符：")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 24, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        nowTime = time.strftime ( "%Y%m%d_%H_%M_%S" )
        nickname = 'heyu'+nowTime
        email = 'heyu'+nowTime+'@qq.com'
        print(email)
        payload = {'email': email,'password': 'aaa$$111','displayname': 'heyu','nickname': nickname,'equipment_number': 'PE-TL10',}
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 24, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 24, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 24, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 24, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )

        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

if __name__ == '__main__':
    unittest.main ()









