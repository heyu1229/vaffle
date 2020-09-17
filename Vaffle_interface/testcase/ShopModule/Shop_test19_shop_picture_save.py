# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------管理我的店铺 - 图片/视频上传----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------管理我的店铺 - 图片上传----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 22
        member_id='7238fc91-0b5e-4f14-8288-95f60dae7658'
        print ("testcase_001管理我的店铺 - 图片上传:")

        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload = {"shop_id": "54273", "images":images,'normal_member_uuid':'b9f73f23-7bc6-4de6-9f9b-df2c98076221'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------管理我的店铺 - 视频上传----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 23
        member_id='7238fc91-0b5e-4f14-8288-95f60dae7658'
        print ("testcase_002管理我的店铺 - 视频上传:")

        payload = {"shop_id": "54273", "video": "posts/1505153294565_832_android.mp4",
                   "video_cover":'posts/1505153294565_832_android.jpg',"video_cover_ratio":1.00,
                   'normal_member_uuid':'b9f73f23-7bc6-4de6-9f9b-df2c98076221'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()