# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------修改用户头像---------------------------
class Avatar(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------用户头像上传保存成功----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 45
        print("testcase001用户头像上传保存成功：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        print ( "msg返回值：save success" )


if __name__ == '__main__':
    unittest.main()
