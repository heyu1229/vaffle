# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc
import time,sys
import global_list
sys.path.append(global_list.path+"/public_1")
import xlrd
from get_token import Token
from get_url import Url
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#---------------邮箱验证码校验----------------------
class Codecheck(unittest.TestCase):

    def setUp(self):

        #路径
        self.url = Url().test_url()
        self.member_id = '452'
        self.email ='1929996@omv.com'
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------邮箱验证码校验正确forgot----------------------------------
    def testcase_001(self):

        # -----------------先获取验证码---------------------------------
        # 获取路径
        url1 = self.obi.read_excel_data ( 0, 79, 4,self.filename )
        # 原地址+当前接口地址拼接
        url1 = self.url + url1
        print(url1)
        payload = {"email": "1929996@omv.com"}
        token = Token ().test_token1 ( payload, self.member_id )
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token': token,
                   'login': self.member_id}
        r = requests.post ( url1, params=payload, headers=headers )
        result = r.json ()
        self.obj.write_excel_data ( 0, 79, 6, result['code'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 79, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 79, 8, str ( result ),self.path,self.filename )
        identifycode = result['data']['code']

        # 获取路径
        url1 = self.obi.read_excel_data ( 0, 90, 4 ,self.filename)
        # 原地址+当前接口地址拼接
        url1 = self.url + url1
        print(url1)
        payload = {'email': self.email,'code': identifycode,'type': 'forgot'}
        token = Token ().test_token1 ( payload, self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token': token,
                   'login': self.member_id}
        r = requests.post ( url1, params=payload, headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 90, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 90, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 90, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 90, 9, end - start,self.path,self.filename )



        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")



    #-----------------邮箱验证码校验失败----------------------------------
    def testcase_002(self):
        # 获取路径
        url1 = self.obi.read_excel_data ( 0, 92, 4,self.filename )
        # 原地址+当前接口地址拼接
        url1 = self.url + url1
        payload = {"email":"1929995@omv.com","code": "111111","type": "forgot"}
        token = Token ().test_token1 ( payload, self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token': token,
                   'login': self.member_id}
        r = requests.post ( url1, params=payload, headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 92, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 92, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 92, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 92, 9, end - start,self.path,self.filename )

        self.assertEqual(10009, result['code'])
        print("code返回值：10009")
        self.assertEqual('Verification Code Error', result['msg'])
        print("msg返回值：Verification Code Error")


if __name__ == '__main__':
    unittest.main()