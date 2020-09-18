# -*- coding:UTF-8 -*-
import unittest,json
import requests
import time,gc,sys


from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#---------------举报用户----------------------
class System_nation(unittest.TestCase):

    def setUp(self):
        self.member_uuid = Url ().test_user ()
        self.requests = FuncRequests ()

 # -----------------举报用户----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 24
        print("testcase_001举报用户：")
        s1 = "update vaffle.vape_member_report_record set status=0 where report_member_id='746'"
        execute_sql1 = self.requests.sql_vaffle(s1)
        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload={"report_member_uuid":"4e802cdb-5bf2-44b1-90e4-791dacac93f4","reason_id":1,"reason":"reason1","images":images}
        result=self.requests.interface_requests_payload(self.member_uuid,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
 #
 # # -----------------重复举报用户----------------------------------
 #    def testcase_002(self):
 #        sheet_index = 3
 #        row = 25
 #        print("testcase_002重复举报用户：")
 #        member_id = "745"
 #        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
 #               {"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},
 #               {"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
 #        images = json.dumps(obj)
 #        payload={"report_member_id":746,"reason_id":1,"reason":"reason1","images":images}
 #        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)
 #
 #        self.assertEqual(10130, result["code"])
 #        print("code返回值：10130")

if __name__=="__main__":
    unittest.main()