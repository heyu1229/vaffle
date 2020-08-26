# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------发送邀请----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------发送邀请---------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 3

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 发送邀请:")
        member_uuid={'e51ae55c-6131-4d20-a31e-6595a932c84b'
                     }
        a=0
        start = time.time()
        for n in member_uuid:
            print("n=",n)
            payload={"guid":"48afaa46-0d80-4518-a880-3577530440d0","member_uuid":n}
            result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)
            a=a+1
            print("a=",a)
        end = time.time()
        self.assertEqual(10000, result['code'])
        print("花费时间：",end-start)

if __name__ == "__main__":
    unittest.main()