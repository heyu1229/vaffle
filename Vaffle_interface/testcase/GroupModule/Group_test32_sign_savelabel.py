# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------注册页面标签页写入----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------注册页面标签页写入--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 41
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 注册页面标签页写入:")

        obj = (1,2)
        label_id = json.dumps(obj)
        payload = {'label_id':label_id}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()