# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------提交店铺纠错信息----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.requests = FuncRequests()
       self.member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

    #-----------------店铺纠错信息提交成功----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 6
        print ("testcase_001提交店铺纠错信息:")

        s = 'delete from vape_shop_correction where shop_id=1315 and member_id=960'
        self.requests.sql_vaffle_post(s)

        obj = ({"week":[1,2],"start":"01:00","close":"03:00"},{"week":[4,5],"start":"05:00","close":"06:00"})
        business_hours = json.dumps(obj)
        payload = {"shop_id":"1315","tel":"18888066666","address":"address111","shop_name":"shop_name111","business_hours":business_hours,"other":" 111"}
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()