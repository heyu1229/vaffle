# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------post动态详情推荐贴----------------------
class posts_detail_recommend(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------post动态详情推荐贴----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 62
        print("testcase_001 post动态详情推荐贴：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'type':'post','post_id':98713,'page':1,'member_uuid':member_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()