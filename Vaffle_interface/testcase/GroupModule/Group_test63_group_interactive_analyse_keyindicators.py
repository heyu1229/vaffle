# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#------------------群组数据分析 - 互动【单独获取 关键指标】----------------------
class Group_noticedel(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #----------------------群组数据分析 - 互动【单独获取 关键指标】--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 74
        print("testcase_001 群组数据分析 - 互动【单独获取 关键指标】:")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'guid':'48afaa46-0d80-4518-a880-3577530440d0','start_date':'20200101','end_date':'20200818'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()