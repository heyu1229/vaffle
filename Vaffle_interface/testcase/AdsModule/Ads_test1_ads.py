# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------广告----------------------
class Ads(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------post广告----------参数值：0.5625或0.625------------------------
    def testcase_001(self):
        sheet_index = 10
        row = 1
        member_id='none'
        print ("testcase_001 post广告:")
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------discover广告----------参数值：0.5625或0.625------------------------
    def testcase_002(self):
        sheet_index = 10
        row = 4
        member_id='none'
        print ("testcase_002 discover广告:")
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------发现群组广告----------参数值：0.5625或0.625------------------------
    def testcase_003(self):
        sheet_index = 10
        row = 6
        member_uuid = "acaf5442-c321-46ee-b3d8-29f563c405c2"
        print ("testcase_003 发现群组广告:")
        payload={"ratio":"0.625","advert":"discovergroup"}
        result=self.r.interface_requests_payload(member_uuid,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------relationposts广告----------参数值：0.5625或0.625------------------------
    def testcase_004(self):
        sheet_index = 10
        row = 6
        member_uuid = "acaf5442-c321-46ee-b3d8-29f563c405c2"
        print ("testcase_004 relationposts广告:")
        payload={"ratio":"0.625","advert":"relationposts"}
        result=self.r.interface_requests_payload(member_uuid,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()