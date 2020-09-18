# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------仲裁申诉问题页面列表----------------------
class System_feedback(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------反馈----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 30
        print("testcase_001 反馈：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {'type':'feedback'}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------用户申诉----------------------------------
    def testcase_002(self):
        sheet_index = 3
        row = 31
        print("testcase_002 用户申诉：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {'type':'arbitrate'}
        member_id = "92fe76f8-6b8d-4c5b-9fb1-99f4407afe9"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
if __name__=="__main__":
    unittest.main()