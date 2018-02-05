# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc
import xlrd,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from get_token import Token
from get_url import Url
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
#---------------兑换优惠---------------------
class RewardsDescription(unittest.TestCase):

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
    #-----------------兑换优惠积分不足--------------------------------
    def testcase_001(self):
        #获取路径
        url1 = self.obi.read_excel_data ( 8, 6, 4,self.filename)
        #原地址+当前接口地址拼接
        url1 = self.url +url1
        payload =self.obi.read_excel_data_dict ( 8, 6, 5,self.filename)
        token = Token ().test_token1 ( payload,self.member_id )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        end = time.time ()
        result=r.json()
        print(r)
        self.obj.write_excel_data ( 8, 6, 9, end - start ,self.path,self.filename)

        self.obj.write_excel_data( 8, 6, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 8, 6, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 8, 6, 8, str(result),self.path,self.filename)

        self.assertEqual(10041, result['code'])
        print("code返回值：10041")

        self.assertEqual('Your points are insufficient.', result['msg'])
        print("msg返回值：Your points are insufficient.")



    # -----------------用户兑换等级不够-------422等级为最低级-------------------------
    def testcase_002(self):
        # 获取路径
        url1 = self.obi.read_excel_data ( 8, 7, 4 ,self.filename)
        # 原地址+当前接口地址拼接
        url1 = self.url + url1
        payload = self.obi.read_excel_data_dict ( 8, 7, 5,self.filename )
        token = Token ().test_token1 ( payload, '422' )
        start = time.time ()
        headers = {'device': 'android ', 'version': self.version, 'lang': 'en', 'timestamp': '1493780505','token': token, 'login': '422'}
        r = requests.post ( url1, params=payload, headers=headers )
        result=r.json()
        print(result)
        end = time.time ()
        self.obj.write_excel_data( 8, 7, 6, result['code'],self.path,self.filename)
        self.obj.write_excel_data ( 8, 7, 7, result['msg'] ,self.path,self.filename)
        self.obj.write_excel_data ( 8, 7, 8, str(result),self.path,self.filename)
        self.obj.write_excel_data ( 8, 7, 9, end - start,self.path,self.filename )

        self.assertEqual(10041, result['code'])
        print("code返回值：10041")

        self.assertEqual("Your points are insufficient.", result['msg'])
        print("msg返回值：Your points are insufficient.")

if __name__ == '__main__':
    unittest.main()