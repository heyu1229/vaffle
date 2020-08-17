# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------综合搜索 hashtag搜索/search/integrate----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------综合搜索-hashtag搜索--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 29
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 综合搜索-hashtag搜索:")

        payload = {"page":1,'keywords':'beth','type':'hashtag'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------综合搜索-群组搜索--------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 30
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 综合搜索-群组搜索:")

        payload = {"page":1,'keywords':'queen','type':'group','search_range':'all'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()