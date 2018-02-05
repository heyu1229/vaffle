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
#---------------用户个人post列表--------vape_posts表 type:2.2.0接口只有all------------
class List(unittest.TestCase):

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

    #-----------------用户个人post列表 all----------------------------------
    def testcase_001(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 71, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 71, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 71, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 71, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 0, 71, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 71, 9, end - start ,self.path,self.filename)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


    #-----------------用户个人post列表第2页数据----------------------------------
    def testcase_002(self):
        #先获取第一页最后一条post的post_id
        url1 = Read_ExcelData().read_excel_data(0, 71, 4, self.filename)
        # 原地址+当前接口地址拼接
        url1 = self.url + url1
        payload1 = Read_ExcelData().read_excel_data_dict(0, 71, 5, self.filename)
        token1 = Token().test_token1(payload1, self.member_id)
        start = time.time()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505',
                   'token': token1, 'login': self.member_id}
        r1 = requests.post(url1, params=payload1, headers=headers)
        result1 = r1.json()
        date=result1['data']['list']
        post_id=date[9]['post_id']


        #原地址+当前接口地址拼接
        payload ={"page": "2","type":"all","member_id": "744","last_id":post_id}
        token = Token ().test_token1 (payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 72, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 72, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 72, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 72, 9, end - start,self.path,self.filename )

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    # -----------------type不存在----------------------------------
    def testcase_004(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 0, 74, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 0, 74, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 0, 74, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 0, 74, 7, result['msg'],self.path,self.filename )
        self.obj.write_excel_data ( 0, 74, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 0, 74, 9, end - start ,self.path,self.filename)

        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

            


if __name__ == '__main__':
    unittest.main()