# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------消息中心 - 通知列表- 阅读记录上传---------------------
class Message(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------消息中心 - 通知列表- 阅读记录上传----------------------------------
    def testcase_001(self):
        sheet_index = 5
        row = 16
        print("testcase_001 消息中心 - 通知列表- 阅读记录上传：")

        #发布一个post
        member_id1 = '606e2b84-96a5-4d48-8abc-db9ac600caf3'
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"content": "接口在" + date + "测试阅读记录上传", "images": images, "category": "post"}
        urlpart1 = '/posts/publish'
        result1 = self.r.interface_requests_data(member_id1,urlpart1,payload1)
        print('code=',result1['code'])
        post_id = result1['data']['post_id']
        time.sleep(5)

        #获取notice_id
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload2 = {'page':1}
        urlpart2 = '/newnoticelist'
        result2 = self.r.interface_requests_data(member_id,urlpart2,payload2)
        notice_id = result2['data']['list'][0]['notice_id']
        print('notice_id=',notice_id)

        #删除post
        payload3 = {'post_id':post_id}
        urlpart3 = '/posts/del'
        result3 = self.r.interface_requests_data(member_id1,urlpart3,payload3)
        print('code=',result3['code'])

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'notice_id':'notice_id'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()