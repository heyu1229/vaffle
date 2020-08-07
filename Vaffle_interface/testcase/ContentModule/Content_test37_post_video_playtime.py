# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------记录视频播放时间----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------记录视频播放时间----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 51
        print("testcase_001 记录视频播放时间：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        obj = ({"video_total_time": "100", "member_id":member_id, "post_id": 46,"play_time":60},)
        p = json.dumps(obj)
        payload = {"p":p}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()