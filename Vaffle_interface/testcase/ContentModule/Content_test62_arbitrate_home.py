# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

    #---------------众裁厅---------------------
class arbitrate_home(unittest.TestCase):
    def setUp(self):
        self.r = FuncRequests()

    def testcase_001(self):
        sheet_index = 1
        row = 82
        print("testcase_001 众裁厅：")
        payload = {"page":1,"pageSize":2,"orderBy":1}
        member_id = "a5f10151-5685-4432-8c35-7198bc6511c9"

        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()