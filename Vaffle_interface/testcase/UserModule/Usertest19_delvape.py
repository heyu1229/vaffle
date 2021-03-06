# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#------------------------电子烟设备删除---------------------------
class Delvape(unittest.TestCase):

    def setUp(self):
        #路径
        self.url = Url().test_url()
        self.member_uuid = Url().test_user()
        self.requests = FuncRequests()
    #-----------------电子烟设备批量删除--vape_member_vape_device表--------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 19
        print("testcase001 电子烟设备批量删除：")
        obj = ('960','961')
        top_ids = json.dumps(obj)
        payload = {'ids': top_ids}
        result = self.requests.interface_requests_payload(self.member_uuid,sheet_index,row,payload)
        self.assertEqual ( 10000, result['code'] )
        print ( "code返回值：10000" )
        self.assertEqual ( '', result['msg'] )
        print ( "msg返回值：ok" )

        #清缓存
        url2 =self.url+"/delmembercache"
        payload ={}
        headers ={}
        r = requests.get ( url2, params=payload, headers=headers )


if __name__ == '__main__':
    unittest.main()