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

#---------------产品 - 删除产品----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------产品 - 删除一个产品----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 34
        member_id='10394'
        print ("testcase_001删除一个产品:")

        # 调用新增产品接口发送一条动态，获取product_ids
        product_ids = product()

        payload={ "shop_id": 29388, "product_ids":product_ids,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

   #-----------------产品 - 删除多个产品----------------------------------
    def testcase_002(self):
        sheet_index = 12
        row = 35
        member_id='10394'
        print ("testcase_001删除一个产品:")

        # 调用新增产品接口发送一条动态，获取product_ids
        product_id1=product()
        product_id2=product()
        product_id3=product()
        product_ids=str(product_id1)+','+str(product_id2)+','+str(product_id3)
        print("product_ids=",product_ids)


        payload={ "shop_id": 29388, "product_ids":product_ids,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #-----------------产品 - 删除一个产品----------------------------------
    def testcase_003(self):
        sheet_index = 12
        row = 44
        member_id='34791'
        print ("testcase_003其他管理员删除一个产品:")

        # 调用新增产品接口发送一条动态，获取product_ids
        product_ids = product()

        payload={ "shop_id": 29388, "product_ids":product_ids,"normal_member_id":745}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()


def product():
    # 调用新增产品接口发送一条动态，获取product_ids
    r = FuncRequests()
    for index in range(0, 2):
        member_id = '10394'
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"name": "autotest" + date, "description": "description" + date, "images": images,
                    "shop_id": 29388,"normal_member_id":745}
        # 获取发布接口token值
        urlpart1 = '/product/add'
        result1 = r.interface_requests_data(member_id, urlpart1, payload1)
        product_id = result1["data"]["product_id"]
        return product_id