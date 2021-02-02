# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------动态点赞/取消点赞----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------动态点赞----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 8
        # 调用发布接口发送一条动态，获取post_id
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        # member_id = "a5f10151-5685-4432-8c35-7198bc6511c9"
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布post用于点赞和取消点赞", "images": images, "category": "post"}
        # 获取发布接口token值
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        global post_id
        post_id = result1["data"]["post_id"]


        print ("testcase_001动态点赞:")
        payload = {'post_id':post_id,"praise_state":1}
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------动态取消点赞----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 9
        print ("testcase_002 动态取消点赞:")
        payload = {'post_id':post_id,"praise_state":0}
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
