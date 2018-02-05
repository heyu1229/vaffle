# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import global_list
sys.path.append(global_list.path+"/public_1")
import time

import xlrd
from get_token import Token
from get_url import Url
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#------------------------保存用户的电子烟设备---------------------------
class SaveDevice(unittest.TestCase):

    def setUp(self):
        #路径
        self.url = Url().test_url()
        self.member_id = '744'
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------保存现有的电子烟设备verified----------------------------------
    def testcase_001(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 65, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 65, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version':self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 65, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 65, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 65, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 65, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )


    #-----------------保存DIY正在审核中的电子烟设备pending----------------------------------
    def testcase_002(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 66, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 66, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 66, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 66, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 66, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 66, 9, end - start ,self.path,self.filename)

        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )


    #-----------------保存审核未通过的电子烟设备not_passed----------------------------------
    def testcase_003(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 67, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 67, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 67, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 67, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 67, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 67, 9, end - start,self.path,self.filename )


        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )


    #-----------------brand_name 特殊字符----------------------------------
    def testcase_004(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 68, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 68, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 68, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 68, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 68, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 68, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )


    #-----------------type_name 特殊字符----------------------------------
    def testcase_005(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 69, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 69, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 69, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 69, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 69, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 69, 9, end - start,self.path,self.filename )

        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )

if __name__ == '__main__':
    unittest.main()