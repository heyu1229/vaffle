# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
import time

import xlrd
from get_token import Token
from get_url import Url
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#------------------------用户重置密码---------------------------
class ResetPass(unittest.TestCase):

    def setUp(self):
        #路径
        self.url = Url().test_url()
        self.member_id = '452'
        self.email = '1929996@omv.com'
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()

    # -----------------新密码与旧密码一致----------------------------------
    def testcase_001(self):
        # -----------------先获取验证码---------------------------------
        # 获取路径
        url1 = self.obi.read_excel_data ( 0, 79, 4 ,self.filename)
        # 原地址+当前接口地址拼接
        url1 = self.url + url1
        payload = {"email": "1929996@omv.com"}
        token = Token ().test_token1 ( payload, self.member_id )
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token': token,'login': self.member_id}
        r = requests.post ( url1, params=payload, headers=headers )
        result = r.json ()
        self.obj.write_excel_data ( 0, 79, 6, result['code'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 79, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 79, 8, str ( result ) ,self.path,self.filename)
        identifycode = result['data']['code']

        # 获取路径
        url1 = self.obi.read_excel_data ( 0, 83, 4 ,self.filename)
        # 原地址+当前接口地址拼接
        url1 = self.url + url1
        payload = {"email": "1929996@omv.com", "password": "123456", "code": identifycode}
        token = Token ().test_token1 ( payload, self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token': token,
                   'login': self.member_id}
        r = requests.post ( url1, params=payload, headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 83, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 83, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 83, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 83, 9, end - start ,self.path,self.filename)


        self.assertEqual(10032, result['code'])
        print("code返回值：10032")
        self.assertEqual('The password is the same as the old one, so please input another one.', result['msg'])
        print("msg返回值：The password is the same as the old one, so please input another one.")


    # -----------------验证码超长----------------------------------
    def testcase_002(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 84, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 84, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 84, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 84, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 84, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 84, 9, end - start,self.path,self.filename )

        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.',result['msg'])
        print("msg返回值：Time out.")


    # -----------------验证码为空----------------------------------
    def testcase_003(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 85, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 85, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 85, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 85, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 85, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 85, 9, end - start,self.path,self.filename )


        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.',result['msg'])
        print("msg返回值：Time out.")

    #-----------------账户不存在----------------------------------

    def testcase_004(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 86, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 86, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 86, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 86, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 86, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 86, 9, end - start,self.path,self.filename )

        self.assertEqual(10004, result['code'])
        print("code返回值：10004")

        self.assertEqual("The mailbox or nickname has not been registered, so please sign up.", result['msg'])
        print("msg返回值：The mailbox or nickname has not been registered, so please sign up.")




    # -----------------验证码错误----------------------------------
    def testcase_005(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 87, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 87, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 87, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 87, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 87, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 87, 9, end - start ,self.path,self.filename)


        self.assertEqual(10008, result['code'])
        print("code返回值：10008")
        self.assertEqual('Invalid verification code, please resend.',result['msg'])
        print("msg返回值：Invalid verification code, please resend.")

if __name__ == '__main__':
    unittest.main()





