# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------用户反馈----------------------
class System_feedback(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------用户反馈----------------------------------
    def testcase_001(self):
        sheet_index = 3
        row = 2
        print("testcase_001用户反馈：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        payload = {"issue": "接口在"+date+"测试用户反馈","topic": 4,'type':'feedback'}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------用户申诉----------------------------------
    def testcase_002(self):
        # s = 'update vape_post_report set status=6,is_appeal=0 where id =2111'
        # s1 = 'delete from vape_arbitrate_appeal where report_id=2111'
        # self.r.sql_vaffle_post(s)
        # self.r.sql_vaffle_post(s1)
        sheet_index = 3
        row = 3
        print("testcase_002 用户申诉：")
        date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},
               {"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload = {"issue": "接口在"+date+"测试用户反馈","topic": 11,'type':'arbitrate','report_id':'2151',
                   'aztec_images':images}
        member_id = "92fe76f8-6b8d-4c5b-9fb1-99f4407afe96"
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")
if __name__=="__main__":
    unittest.main()