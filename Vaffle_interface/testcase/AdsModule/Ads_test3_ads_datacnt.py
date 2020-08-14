# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------广告数据统计----------------------
class Ads(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------广告数据统计----------------------------------
    def testcase_001(self):
        sheet_index = 10
        row = 4
        member_id='none'
        print ("testcase_001 广告数据统计:")
        obj = ({"ad_id": 123, "view_num": 2, "click_num": 3},)
        data = json.dumps(obj)
        payload={"data":data}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()