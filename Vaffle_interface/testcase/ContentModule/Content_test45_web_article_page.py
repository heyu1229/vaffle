# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------单文档页面内容----------------------
class web_article_page(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------单文档页面内容----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 60
        print("testcase_001 单文档页面内容：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        payload = {'code':'4OaT9Q','type':1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()