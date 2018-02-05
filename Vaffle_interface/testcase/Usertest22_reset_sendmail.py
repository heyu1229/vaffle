# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc

import time,sys

import xlrd
import global_list
sys.path.append(global_list.path+"/public_1")
from get_token import Token
from get_url import Url
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#------------------------用户重置密码验证码发送邮件---------------------------
class ResetSendmail(unittest.TestCase):

    def setUp(self):
        #路径
        self.url = Url().test_url()
        self.member_id = '453'
        self.email = '1929995@omv.com'
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()

    #-----------------用户重置密码发送验证码----------------------------------
    def testcase_001(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 79, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 79, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 79, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 79, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 79, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 79, 9, end - start ,self.path,self.filename)
        identifycode = result['data']['code']
        print(identifycode)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('send success', result['msg'])
        print("msg返回值：send success")


    # -----------------用户重置密码成功-22：resetpass接口---------------------------------
        # 获取路径
        url1 = self.obi.read_excel_data ( 0, 80, 4 ,self.filename)
        # 原地址+当前接口地址拼接
        url1 = self.url + url1
        password =time.strftime ( "%Y%m%d_%H_%M_%S" )
        payload = {"email": "1929995@omv.com","password":password,"code": identifycode}
        token = Token ().test_token1 ( payload, self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505','token': token, 'login': self.member_id}
        r = requests.post ( url1, params=payload, headers=headers )
        result = r.json ()
        print ( result )
        end = time.time ()
        self.obj.write_excel_data ( 0, 80, 6, result['code'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 80, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 80, 8, str ( result ) ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 80, 9, end - start,self.path,self.filename )

        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：Reset password successfully" )



    #-----------------账户不存在----------------------------------
    def testcase_002(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 81, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 81, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 81, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 81, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 81, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 81, 9, end - start ,self.path,self.filename)
        self.assertEqual(10004, result['code'])
        print("code返回值：10004")

        self.assertEqual("The mailbox or nickname has not been registered, so please sign up.", result['msg'])
        print("msg返回值：The mailbox or nickname has not been registered, so please sign up.")

    #-----------------非法账户----------------------------------
    def testcase_003(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 82, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 82, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 82, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 82, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 82, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 82, 9, end - start ,self.path,self.filename)

        self.assertEqual(9999, result['code'])
        print("code返回值：9999")

        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

        gc.collect()
if __name__ == '__main__':
    unittest.main()




