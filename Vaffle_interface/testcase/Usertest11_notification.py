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
#------------------------消息通知是否开启接收设置  ---------------------------
class Notification(unittest.TestCase):

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
    #-----------------消息通知接收全开启----------------------------------
    #-------------vape_member_switch表  1:followers 2:attention 3:like 4:comment 5:sound-  setting 1开启 0关闭-------------
    def testcase_001(self):

        #获取路径
        url1 = self.obi.read_excel_data ( 0, 46, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 46, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 46, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 46, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 46, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 46, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )

        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

    # -----------------消息通知接收全关闭----------------------------------
    def testcase_002(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 47, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 47, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 47, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 47, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 47, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 47, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )

        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

    # -----------------消息通知followers字段为数字----------------------------------
    def testcase_003(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 48, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 48, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 48, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 48, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 48, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 48, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )

        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )


    # -----------------消息通知attention字段为数字+字母----------------------------------
    def testcase_004(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 49, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 49, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 49, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 49, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 49, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 49, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------消息通知like字段为aaa----------------------------------
    def testcase_005(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 50, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 50, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version':self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 50, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 50, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 50, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 50, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

    # -----------------消息通知comment字段为特殊字符----------------------------------
    def testcase_006(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 51, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 51, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 51, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 51, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 51, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 51, 9, end - start ,self.path,self.filename)


        self.assertEqual ( 9999, result['code'] )
        print ( "code返回值：9999" )
        self.assertEqual ( 'Time out.', result['msg'] )
        print ( "msg返回值：Time out." )

if __name__ == '__main__':
    unittest.main()
