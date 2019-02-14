# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time,gc,xlrd
import json
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests
#---------------播放视频列表----------------------
class VideoList(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------播放视频列表post----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 9
        print("testcase_001播放视频列表post：")

        member_id="960"
        payload = {"post_id": 290178,"page": "1","type": "post"}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------播放视频列表me----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 10
        print("testcase_002播放视频列表me：")
        member_id = "960"

        payload = {"post_id": 290178, "page": "1", "type": "me"}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()