# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------创建/更新相册接口----------------------
class Group_noticedel(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------创建相册接口--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 50
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 创建相册接口:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {'title': 'title'+date,'description':'description'+date,'guid':'48afaa46-0d80-4518-a880-3577530440d0'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)
        global album_id
        album_id = result['data']['album_id']
        print('album_id=',album_id)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------更新相册接口--------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 51
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_002 更新相册接口:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {'album_id':album_id,'title': '更新title'+date,'description':'更新description'+date,'guid':'48afaa46-0d80-4518-a880-3577530440d0'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()