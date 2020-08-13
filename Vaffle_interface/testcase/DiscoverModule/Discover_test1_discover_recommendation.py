# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------发热门搜索hot searches----------------------
class Discover_recommendation(unittest.TestCase):

    def setUp(self):
        self.member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        self.requests = FuncRequests()

    #-----------------discover页推荐数据（用户、店铺）----------------------------------
    def testcase_001(self):
        sheet_index =4
        row = 1
        print("testcase001 discover页推荐数据（用户、店铺）：")
        payload = {"lat":"31","lon":"121"}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()
