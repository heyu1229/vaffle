# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------发布评论----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------评论列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 11
        # 1.调用发布接口发送一条动态，获取post_id
        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试发布post用于发布评论", "images": images, "category": "post"}
        # 获取发布接口token值
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        post_id = result1["data"]["post_id"]

        #2.发布评论
        urlpart2 = '/comments/publish'
        payload2 = {'post_id':post_id,"content":"接口测试发布评论内容"+date}
        result2=self.r.interface_requests_data(member_id, urlpart2, payload2)

        print("testcase_001 评论列表:")
        payload = {'post_id': post_id, "page": 1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
