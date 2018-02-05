# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
sys.path.append(global_list.path+"/log")
from interface_log import interface_log

#---------------品牌型号数据----------------------
class Brands(unittest.TestCase):

    def setUp(self):
        # 获取EXcel路径
        self.path = Url ().test_path ()
        # 打开excel
        self.filename = "aa"

        #路径
        url = Url().test_url()
        self.obi = Read_ExcelData()

        self.base_url = self.obi.read_excel_data(1, 1, 4,self.filename)
        self.base_url1=url+self.base_url
        self.LOG = interface_log.init_log ( 0 )
        #获取版本
        self.version =Version().test_version()

    #-----------------品牌型号数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 1
        print ("testcase_001品牌型号数据测试:")
        #获取token值
        payload = self.obi.read_excel_data_dict(sheet_index,row,5,self.filename)
        member_id="744"
        token = Token().test_token1(payload,member_id)

        start=time.time()
        headers = {"device": "android ","version": self.version,"lang": "en","timestamp": "1493780505","token":token,"login":member_id}
        try:
            r = requests.post(self.base_url1,headers=headers)
            result=r.json()
            format_result = json.dumps ( result, indent=1 );
            print(format_result)
            self.LOG.debug("Content_test1_Brands:%s" % format_result)
        except Exception as e:
            self.LOG.error("Content_test1_Brands failed")
        end = time.time()

        #写入excel中
        str_result=str(result)
        obj = Write_ExcelData()
        obj.write_excel_data(sheet_index, row, 6, result["code"],self.path,self.filename)
        obj.write_excel_data(sheet_index, row,10, end-start,self.path,self.filename)

        if len(str_result)>32767:
            obj.write_excel_data(sheet_index, row, 8, str_result[0:32767],self.path,self.filename)
            obj.write_excel_data(sheet_index, row, 9, str_result[32767:],self.path,self.filename)
        else:
            obj.write_excel_data(sheet_index, row, 8, str_result,self.path,self.filename)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
        # try:
        self.assertEqual("", result["msg"])
        print("msg返回值：ok")
        obj.write_excel_data(sheet_index, row, 7, "ok",self.path,self.filename)
        # except AssertionError as e:
        #     print("msg返回报错:",result["msg"])
        #     Write_ExcelData().write_excel_data(sheet_index, row, 7, result["msg"],self.path,self.filename)


if __name__ == "__main__":
    unittest.main()