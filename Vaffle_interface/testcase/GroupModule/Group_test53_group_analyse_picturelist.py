# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#------------------【群组post帖子分析-图片/视频 】 列表----------------------
class Group_noticedel(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #----------------------【群组post帖子分析-图片/视频 】 列表--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 64
        print("testcase_001 【群组post帖子分析-图片/视频 】 列表:")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'post_id':98330}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()