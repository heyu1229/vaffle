# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------申请成为店铺店主----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------普通用户申请成为店铺店主----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 26
        member_id='202aedd8-0681-478c-8544-50070db8b53a'
        print ("testcase_001普通用户申请成为店铺店主:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "接口测试店铺"+date, "nation": "china","city": "shangai","address": "qilianshanlu",
                   "first_name": "first_name","last_name": "last_name","img_card_front":"posts/1512710644871_767_android.jpg",
                   "img_card_back":"posts/1512710644871_767_android.jpg","img_license":"posts/1512710644871_767_android.jpg",
                   "is_boss":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10095, result['code'])
            print("code返回值：10095")

    #-----------------普通用户认领店铺----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 27
        member_id='4e802cdb-5bf2-44b1-90e4-791dacac93f4'
        print ("testcase_002普通用户认领店铺:")

        s = 'delete from vape_shop_keeper_apply where member_id=746 and shop_id=29388'
        self.r.sql_vaffle_post(s)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "接口测试店铺"+date, "nation": "china","city": "shangai","address": "qilianshanlu",
                   "first_name": "first_name","last_name": "last_name","img_card_front":"posts/1512710644871_767_android.jpg",
                   "img_card_back":"posts/1512710644871_767_android.jpg","img_license":"posts/1512710644871_767_android.jpg",
                   "is_boss":1,"apply_shop_id":29388,"normal_member_uuid":'4e802cdb-5bf2-44b1-90e4-791dacac93f4'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except:
            self.assertEqual(10095, result['code'])
            print("code返回值：10095")

if __name__ == "__main__":
    unittest.main()