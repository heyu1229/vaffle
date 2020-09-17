# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------店铺连锁店----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------店铺连锁店----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 35
        member_id='7238fc91-0b5e-4f14-8288-95f60dae7658'
        print ("testcase_001店铺连锁店:")

        payload={ "shop_id": 54273, "page":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()