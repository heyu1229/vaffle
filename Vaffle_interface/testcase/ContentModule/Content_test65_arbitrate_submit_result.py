# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

    #---------------违规贴详情页 -提交众裁结果---------------------
class arbitrate_submit_result(unittest.TestCase):
    def setUp(self):
        self.r = FuncRequests()

    def testcase_001(self):
        t = str(int(time.time()))
        s = "update vape_arbitrate_log set created_at="+t+",status=0,is_expire=0 where id='4203'"
        execute_sql = self.r.sql_vaffle_post(s)
        s1 = "update vape_post_report set created_at="+t+",status=2 where id='1970'"
        execute_sql1 = self.r.sql_vaffle_post(s1)
        sheet_index = 1
        row = 85
        print("testcase_001 提交众裁结果：")
        payload = {"report_id": 1970,"type":1,"suggestion":''}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"

        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()