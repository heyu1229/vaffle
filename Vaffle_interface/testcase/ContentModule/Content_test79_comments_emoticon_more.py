# -*- coding:UTF-8 -*-
import unittest,time
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------问题删除功能---------------------
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#-----------------评论表情包 加号列表-----------
class Question_edit(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()
        self.member_uuid = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

    def testcase_001(self):
        sheet_index = 1
        row = 99

        payload = {"page": 1,"type":"1"}
        result = self.r.interface_requests_payload(self.member_uuid, sheet_index, row, payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()