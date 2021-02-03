# -*- coding:UTF-8 -*-
import unittest
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------产品价格分类列表----------------------
from Vaffle_interface.public_1.get_url import Url


class goods_price_list(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()


    def testcase_001(self):
        sheet_index =15
        row = 7
        result = self.requests.interface_requests(self.member_uuid,sheet_index,row)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
