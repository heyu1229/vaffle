# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------公告删除----------------------
class Group_noticedel(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------公告删除--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 48
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 公告删除:")

        payload1 = {'guid': '48afaa46-0d80-4518-a880-3577530440d0', 'page': 1}
        urlpart1 = '/group/noticelist'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        notice_id = result1['data']['list'][0]['notice_id']
        print('notice_id=',notice_id)

        payload = {'notice_id':notice_id,'guid':'48afaa46-0d80-4518-a880-3577530440d0'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()