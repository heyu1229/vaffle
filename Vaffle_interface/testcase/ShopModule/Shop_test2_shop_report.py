# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------举报商户----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r = FuncRequests ()

    #-----------------举报商户成功----------------------------------
    def testcase_001(self):

        sheet_index = 12
        row = 2
        print ("testcase_001举报商户:")

        s = 'delete from vape_report_shop where shop_id=52862 and member_id=960'
        self.r.sql_vaffle_post(s)
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result = self.r.interface_requests(member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()