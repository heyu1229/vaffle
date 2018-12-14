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

#---------------管理我的店铺 - 店铺主页修改----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------管理我的店铺 - 店铺主页修改----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 28
        member_id='10394'
        print ("testcase_001管理我的店铺 - 店铺主页修改:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj=[{"week":["1","2","3","4","5","6","7"],"start":"09:00","close":"18:00"},]
        business_hours=json.dumps(obj)
        payload = {"name": "IECIE Shanghai Vape Culture Week", "info": "info","cover":"posts/1512710644871_767_android.jpg","business_hours":business_hours,
                   "tel":"15800328065","nation":"China","city":"shanghai","address":"qilianshanlu","payment":"zhifubao",
                   "ins":"www.ins.com","youtube":"www.youtube.com","twitter":"www.twitter.com","website":"www.baidu.com",
                   "facebook":"www.fb1.com","shop_id":"29388","timezone":8,"normal_member_id":745,"is_delivery":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()