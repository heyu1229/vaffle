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
#--------------为第三方账户增加邮箱----------------------
class AddEmail(unittest.TestCase):

    def setUp(self):

        #路径
        self.url = Url().test_url()
        self.member_id = '438'
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename = "aa"
        self.obi = Read_ExcelData ()
        # 获取版本
        self.version = Version ().test_version ()
        self.obj = Write_ExcelData()
    #-----------------为第三方账户增加邮箱成功(手动去数据库vape_members改email :427871220333311@vk)----------------------------------

    def testcase_001(self):
        print("为第三方账户增加邮箱成功;")
        '''
        #vape_members id=438用户的email 改为427871220333311@vk再重新添加邮箱
        sql2 = SQL_vaffle().update_vape_members()
        SQL_SEARCH_1().insert(sql2)
        '''
        #清缓存
        url2 =self.url+"/delmembercache"
        payload ={}
        headers ={}
        r = requests.get ( url2, params=payload, headers=headers )
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 36, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 36, 5,self.filename)
        token = Token ().test_token1 ( payload,"438" )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': "438"}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 36, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 36, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 36, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 36, 9, end - start,self.path,self.filename )


        self.assertEqual(10038, result['code'])
        print("code返回值：10038")

        self.assertEqual("This account's e-mail has already been bound.", result['msg'])
        print("msg返回值：This account's e-mail has already been bound.")

    #-----------------第三方邮箱已存在----------------------------------

    def testcase_002(self):
        print("第三方邮箱已存在;")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 37, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 37, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 37, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 37, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 37, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 37, 9, end - start ,self.path,self.filename)


        self.assertEqual(10038, result['code'])
        print("code返回值：10038")

        self.assertEqual("This account's e-mail has already been bound.", result['msg'])
        print("msg返回值：This account's e-mail has already been bound.")

    #-----------------增加用户邮箱，该邮箱已被其他用户占用----------------------------------

    def testcase_003(self):
        print("增加用户邮箱，该邮箱已被其他用户占用;")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 38, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 38, 5,self.filename)
        token = Token ().test_token1 ( payload,"491")
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': "491"}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 38, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 38, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 38, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 38, 9, end - start ,self.path,self.filename)


        self.assertEqual(10038, result['code'])
        print("code返回值：10038")

        self.assertEqual("This account's e-mail has already been bound.", result['msg'])
        print("msg返回值：This account's e-mail has already been bound.")

    #-----------------增加的邮箱格式不正确----------------------------------

    def testcase_004(self):
        print("增加的邮箱格式不正确;")
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 39, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 39, 5,self.filename)
        token = Token ().test_token1 ( payload,"491" )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': "491"}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 39, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 39, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 39, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 39, 9, end - start ,self.path,self.filename)


        self.assertEqual(9999, result['code'])
        print("code返回值：9999")

        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

if __name__ == '__main__':
    unittest.main()

