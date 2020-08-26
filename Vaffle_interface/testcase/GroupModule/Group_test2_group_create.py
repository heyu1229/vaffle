# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------创建群组----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------创建群组---------------------------
    def testcase_001(self):

        sheet_index = 14
        row = 2
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 创建群组:")

        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"logo":"","cover":"","type":5,"group_description":"group_description","title":"title"+date,"category":1}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()