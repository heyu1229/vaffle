# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------声音开关  vape_member_switch表---------------------------
class Sound(unittest.TestCase):

    def setUp(self):
        self.member_id = '959'
        self.requests = FuncRequests()
    #-----------------开声音----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 9
        print("testcase001开声音：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )



if __name__ == '__main__':
    unittest.main()
