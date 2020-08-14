# -*- coding:UTF-8 -*-
import unittest,time,json
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

if __name__ == "__main__":
    unittest.main()