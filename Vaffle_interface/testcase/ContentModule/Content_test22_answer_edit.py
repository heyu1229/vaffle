# -*- coding:UTF-8 -*-
import unittest,time
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------回答的编辑---------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------回答的编辑----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 33
        print("testcase_001 回答的编辑：")

        # 1.调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布Q/A", "category": "qa"}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        urlpart = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart, payload1)
        print(result1)
        global question_id
        question_id = result1["data"]["question_id"]
        print(question_id)

        # 2.调用发布回答的接口发布一个回答，获得answer_id
        payload1 = {"question_id": question_id, "content": "接口在" + date + "测试回答Q/A"}
        urlpart = '/answer/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart, payload1)
        global answer_id
        answer_id = result1["data"]["answer_id"]
        print("answer_id=", answer_id)

        payload = {"answer_id": answer_id, "content": "接口在" + date + "测试编辑回答Q/A","aztec_images":'[{"androidid":"1532313356301","imageUrl":"https://s3-us-west-2.amazonaws.com/images-omv/posts/1532313355871_767_android.jpg","radio":"1.0000","tag":1}]'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()