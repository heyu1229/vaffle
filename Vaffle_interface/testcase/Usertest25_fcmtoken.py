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
#---------------更新用户的Google fcm token----------------------
class FcmToken(unittest.TestCase):

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
    #-----------------更新用户的Google fcm token----------------------------------

    def testcase_001(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 89, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 89, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 89, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 89, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 89, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 89, 9, end - start,self.path,self.filename )


        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('ok', result['msg'])
        print("msg返回值：ok")



if __name__ == '__main__':
    unittest.main()