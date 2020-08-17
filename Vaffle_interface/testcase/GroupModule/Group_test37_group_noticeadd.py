# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------公告新增，编辑----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------新增公告--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 46
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 新增公告:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {'guid':'48afaa46-0d80-4518-a880-3577530440d0','description':'notice'+date,'is_top':1}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)
        global notice_id
        notice_id = result['data']['notice_id']
        print('notice_id=',notice_id)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------编辑公告--------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 47
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_002 编辑公告:")


        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {'notice_id':notice_id,'guid':'48afaa46-0d80-4518-a880-3577530440d0','description':'编辑notice'+date,'is_top':1}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()