# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
# sys.path.append(global_list.path+"/public_1")
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------品牌型号数据----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------品牌型号数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 1
        member_id='744'
        print ("testcase_001品牌型号数据测试:")

        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
