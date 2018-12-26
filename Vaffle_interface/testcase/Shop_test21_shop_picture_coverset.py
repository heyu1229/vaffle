# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------管理我的店铺 - 设置店铺主图----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------管理我的店铺 - 设置店铺主图----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 26
        member_id='10394'
        print ("testcase_001管理我的店铺 - 设置店铺主图:")

        #调用图片/视频上传接口获得id
        obj1 = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images1 = json.dumps(obj1)
        payload1 = {"shop_id": "29388", "images":images1,"normal_member_id":745}
        urlpart1 = '/shop/picture/save'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        id=result1["data"]["id"]
        print(result1)
        print("id=",id)

        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1, "tag": 1})
        image = json.dumps(obj)
        payload = {"shop_id": "29388", "pid": id,"image":image,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------管理我的店铺 - 其他用户设置店铺主图----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 47
        member_id='34791'
        print ("testcase_002管理我的店铺 - 其他用户设置店铺主图:")

        #调用图片/视频上传接口获得id
        obj1 = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images1 = json.dumps(obj1)
        payload1 = {"shop_id": "29388", "images":images1,"normal_member_id":745}
        urlpart1 = '/shop/picture/save'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        id=result1["data"]["id"]
        print(result1)
        print("id=",id)

        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1, "tag": 1})
        image = json.dumps(obj)
        payload = {"shop_id": "29388", "pid": id,"image":image,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()