# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
import xlrd
from get_token import Token
from get_url import Url
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#-----------------------用户登录接口---------------------------
class SignIn(unittest.TestCase):

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
    #-----------------用邮箱登录成功--------------------------------
    def testcase_001(self):
        print("用邮箱登录成功:")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 25, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 25, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 25, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 25, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 25, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 25, 9, end - start,self.path,self.filename )

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    # -----------------用nickname登录成功--------------------------------
    def testcase_002(self):
        print("用nickname登录成功:")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 26, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 26, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 26, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 26, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 26, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 26, 9, end - start,self.path,self.filename )

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    # -----------------account为空----------------------------------
    def testcase_003(self):
        print("account为空:")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 27, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 27, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version':self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 27, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 27, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 27, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 27, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )

        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------输入的邮箱账号不存在----------------------------------
    def testcase_004(self):
        print("输入的邮箱账号不存在:")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 28, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 28, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 28, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 28, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 28, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 28, 9, end - start,self.path,self.filename )


        self.assertEqual ( 10004, result['code'] )
        print ( "code返回值：10004" )

        self.assertEqual ( "The mailbox or nickname has not been registered, so please sign up.", result['msg'] )
        print ( "msg返回值：The mailbox or nickname has not been registered, so please sign up." )

    # -----------------密码不正确----------------------------------
    def testcase_005(self):
        print("密码不正确:")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 29, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 29, 5,self.filename)
        token = Token ().test_token ( payload )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': 'none'}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 29, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 29, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 29, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 29, 9, end - start,self.path,self.filename )


        self.assertEqual ( 10055, result['code'] )
        print ( "code返回值：10055" )

        self.assertEqual ( 'Password Error', result['msg'] )
        print ( "msg返回值：Password Error" )

if __name__ == '__main__':
    unittest.main()
    











