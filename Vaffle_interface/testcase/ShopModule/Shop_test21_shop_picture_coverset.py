# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------管理我的店铺 - 设置店铺主图----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------管理我的店铺 - 设置店铺主图----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 25
        member_id='7238fc91-0b5e-4f14-8288-95f60dae7658'
        print ("testcase_001管理我的店铺 - 设置店铺主图:")

        #调用图片/视频上传接口获得id
        obj1 = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images1 = json.dumps(obj1)
        payload1 = {"shop_id": "54273", "images":images1,'normal_member_uuid':'b9f73f23-7bc6-4de6-9f9b-df2c98076221'}
        urlpart1 = '/shop/picture/save'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        id=result1["data"]["id"]
        print(result1)
        print("id=",id)

        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1, "tag": 1})
        image = json.dumps(obj)
        payload = {"shop_id": "54273", "pid": id,"image":image,"normal_member_uuid":'b9f73f23-7bc6-4de6-9f9b-df2c98076221'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()