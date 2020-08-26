# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------更新群组封面或logo----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------更新群组封面---------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 8
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 更新群组封面:")

        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload = {"guid":"48afaa46-0d80-4518-a880-3577530440d0","img":images,"type":"cover"}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------更新群组logo---------------------------
    def testcase_002(self):
        sheet_index = 14
        row = 9
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_002 更新群组logo:")

        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload = {"guid": "48afaa46-0d80-4518-a880-3577530440d0", "img": images, "type": "logo"}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()