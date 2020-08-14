# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------对news详情----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------news详情（review类型)----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 44
        print("testcase_001 news详情（review类型)：")

        # 调用发布接口发送一条动态，获取post_id
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布review", "review_title": "review_title"+date,
                    "review_product":"review_product","review_type":"review_type","category": "review"}
        # 获取发布接口token值
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        print(result1)
        post_id = result1["data"]["post_id"]

        payload = {"category": "review", "post_id": post_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

        # -----------------news详情（news类型)----------------------------------

    def testcase_002(self):
        sheet_index = 1
        row = 45
        print("testcase_002 news详情（news类型)：")

        payload = {"category": "news", "post_id": "41931"}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()