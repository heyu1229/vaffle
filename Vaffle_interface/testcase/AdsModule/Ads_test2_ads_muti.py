# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests
#---------------发布页广告（多条）----------------------
class Ads(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------启动广告----------参数值：0.5625或0.625------------------------
    def testcase_001(self):
        sheet_index = 10
        row = 2
        member_id="b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        print ("testcase_001广告:")
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------轮播图----------参数值：0.5625或0.625------------------------
    def testcase_002(self):
        sheet_index = 10
        row = 3
        member_id="b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        print ("testcase_002轮播图:")
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()