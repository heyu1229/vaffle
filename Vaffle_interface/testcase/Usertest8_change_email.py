# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc

import time
import global_list
sys.path.append(global_list.path+"/public_1")
import xlrd
from get_token import Token
from get_url import Url
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#---------------修改用户邮箱----------------------
class ChangeEmail(unittest.TestCase):

    def setUp(self):

        #路径
        self.url = Url().test_url()
        self.member_id = '760'
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------修改用户邮箱成功----------------------------------
    def testcase_001(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 40, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 40, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version':self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 40, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 40, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 40, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 40, 9, end - start,self.path,self.filename )

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    #-----------------修改为已存在的用户邮箱----------------------------------

    def testcase_002(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 41, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 41, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 41, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 41, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 41, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 41, 9, end - start ,self.path,self.filename)


        self.assertEqual(10002, result['code'])
        print("code返回值：10002")

        self.assertEqual('The email address has been taken.', result['msg'])
        print("msg返回值：The email address has been taken.")


    #-----------------修改的邮箱格式不正确----------------------------------

    def testcase_003(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 42, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 42, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 42, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 42, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 42, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 42, 9, end - start,self.path,self.filename )

        self.assertEqual(9999, result['code'])
        print("code返回值：9999")

        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")


if __name__ == '__main__':
    unittest.main()