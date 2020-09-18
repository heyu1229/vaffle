# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url
#------------------【UGC政策】提交申诉-----------------------
class System_baseornew(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

    def testcase_001(self):
        sheet_index = 3
        row = 37
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"type":"2","plead_email":"1004856404@qq.com","con":"aaa","tik":"NVRKVjFxb3ljeXJUb2VMUlZnSzJzc1dUc0hFWmVVbVdqSHZndU5XQ3IwUnJLeEZoNjM5d2l4NGZRckFTRzM0VHFzaVM4eUlDRnc3OXhHekY3SThYVG4vclo0Zk0vcjd2ZS9pcWYxZG83THNaSkVjcUVHMXNBOGdEUUNoVm9YNnRLWGVEdWNKKy82Z0NnQzhLSDFJTTVjWmljbFA1UEVVMlhyeHpCTVBpcUdBPQ=="}
        result=self.requests.interface_requests_payload(self.member_uuid, sheet_index, row,payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()