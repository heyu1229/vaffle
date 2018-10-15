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

#---------------管理我的店铺 - 图片/视频删除----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------管理我的店铺 - 图片/视频删除----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 25
        member_id='745'
        print ("testcase_001管理我的店铺 - 图片/视频删除:")

        #调用图片/视频上传接口获得id
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload1 = {"shop_id": "28175", "images":images}
        urlpart1 = '/shop/picture/save'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        id=result1["data"]["id"]
        print(result1)
        print("id=",id)

        payload = {"shop_id": "28175", "pid": id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()