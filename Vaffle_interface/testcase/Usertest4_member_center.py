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
#------------------------用户个人中心---------------------------
class MemberCenter(unittest.TestCase):

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
    #-----------------查看当前用户信息----------------------------------
    def testcase_001(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 30, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 30, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 30, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 30, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 30, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 30, 9, end - start,self.path,self.filename )

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    #-----------------查看其他用户信息----------------------------------
    def testcase_002(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 31, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 31, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 31, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 31, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 31, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 31, 9, end - start,self.path,self.filename )

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    #-----------------member_id为空----------------------------------

    def testcase_003(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 32, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 32, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 32, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 32, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 32, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 32, 9, end - start ,self.path,self.filename)


        self.assertEqual(10040, result['code'])
        print("code返回值：10040")

        self.assertEqual('This user does not exist.', result['msg'])
        print("msg返回值：This user does not exist.")

    #-----------------member_id不存在----------------------------------

    def testcase_004(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 33, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 33, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 33, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 33, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 33, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 33, 9, end - start,self.path,self.filename )


        self.assertEqual(10040, result['code'])
        print("code返回值：10040")

        self.assertEqual('This user does not exist.', result['msg'])
        print("msg返回值：This user does not exist.")

if __name__ == '__main__':
    unittest.main()

