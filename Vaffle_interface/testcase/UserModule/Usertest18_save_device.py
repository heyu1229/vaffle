# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import global_list
import applehttp2push
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------保存用户的电子烟设备---------------------------
class SaveDevice(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------保存现有的电子烟设备verified----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 65
        print("testcase001 保存现有的电子烟设备verified：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )


    #-----------------保存DIY正在审核中的电子烟设备pending----------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 66
        print("testcase002 保存DIY正在审核中的电子烟设备pending：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )


    #-----------------保存审核未通过的电子烟设备not_passed----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 67
        print("testcase003 保存审核未通过的电子烟设备not_passed：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )


    #-----------------brand_name 特殊字符----------------------------------
    def testcase_004(self):
        sheet_index =0
        row = 68
        print("testcase004 brand_name 特殊字符：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )


    #-----------------type_name 特殊字符----------------------------------
    def testcase_005(self):
        sheet_index =0
        row = 69
        print("testcase005 type_name 特殊字符：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10059, result['code'] )
        print ( "code返回值：10059" )
        self.assertEqual ( 'You have added the device already.', result['msg'] )
        print ( "msg返回值：You have added the device already." )

if __name__ == '__main__':
    unittest.main()