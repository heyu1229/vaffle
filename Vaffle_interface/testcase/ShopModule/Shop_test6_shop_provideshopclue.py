# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------提供店铺线索----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------提供店铺线索----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 8
        print ("testcase_001提供店铺线索:")

        obj = ({"week":[1,2],"start":"01:00","close":"03:00"},{"week":[4,5],"start":"05:00","close":"06:00"})
        business_hours = json.dumps(obj)
        payload = {"cover": "posts/153682373426094_960_ios.jpg", "address": "kangjian", "shop_name":"shop_lisa","business_hours":business_hours,"payment":"zhifubao","tel":"18833255555","shop_id":"1315"}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()