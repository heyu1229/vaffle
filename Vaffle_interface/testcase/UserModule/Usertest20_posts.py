# -*- coding:UTF-8 -*-
import unittest
import requests
import json,gc,sys
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#---------------用户个人post列表--------vape_posts表 type:2.2.0接口只有all------------
class List(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()

    #-----------------用户个人post列表 all----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 71
        print("testcase001 用户个人post列表 all：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")


    #-----------------用户个人post列表第2页数据----------------------------------
    def testcase_002(self):
        urlpart = "/member/posts"
        payload = {"page": "1","type":"all","member_id": "744"}
        result = self.requests.interface_requests_data(self.member_id,urlpart,payload)
        #先获取第一页最后一条post的post_id
        date=result['data']['list']
        post_id=date[9]['post_id']

        #原地址+当前接口地址拼接
        payload ={"page": "2","type":"all","member_id": "744","last_id":post_id}
        sheet_index =0
        row = 72
        print("testcase002 用户个人post列表第2页数据：")
        result = self.requests.interface_requests_payload(self.member_id,sheet_index,row,payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

    # -----------------type不存在----------------------------------
    def testcase_003(self):
        sheet_index =0
        row = 74
        print("testcase003 type不存在：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual(9999, result['code'])
        print("code返回值：9999")
        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

            


if __name__ == '__main__':
    unittest.main()