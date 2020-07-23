# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from func_requests import FuncRequests
#--------------为第三方账户增加邮箱----------------------
class AddEmail(unittest.TestCase):

    def setUp(self):
        #路径
        self.url = Url().test_url()
        self.member_id = '438'
        self.requests = FuncRequests()
    #-----------------为第三方账户增加邮箱成功(手动去数据库vape_members改email :427871220333311@vk)----------------------------------

    def testcase_001(self):
        '''
        #vape_members id=438用户的email 改为427871220333311@vk再重新添加邮箱
        sql2 = SQL_vaffle().update_vape_members()
        SQL_SEARCH_1().insert(sql2)
        '''
        #清缓存
        url2 =self.url+"/delmembercache"
        payload ={}
        headers ={}
        r = requests.get ( url2, params=payload, headers=headers )
        sheet_index =0
        row = 36
        print("testcase001为第三方账户增加邮箱成功：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)

        self.assertEqual(10038, result['code'])
        print("code返回值：10038")

        self.assertEqual("This account's e-mail has already been bound.", result['msg'])
        print("msg返回值：This account's e-mail has already been bound.")

    #-----------------第三方邮箱已存在----------------------------------

    def testcase_002(self):
        sheet_index =0
        row = 37
        print("testcase002第三方邮箱已存在：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10038, result['code'])
        print("code返回值：10038")
        self.assertEqual("This account's e-mail has already been bound.", result['msg'])
        print("msg返回值：This account's e-mail has already been bound.")

    #-----------------增加用户邮箱，该邮箱已被其他用户占用----------------------------------

    def testcase_003(self):
        sheet_index =0
        row = 38
        print("testcase003增加用户邮箱，该邮箱已被其他用户占用：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10038, result['code'])
        print("code返回值：10038")
        self.assertEqual("This account's e-mail has already been bound.", result['msg'])
        print("msg返回值：This account's e-mail has already been bound.")

    #-----------------增加的邮箱格式不正确----------------------------------

    def testcase_004(self):
        sheet_index =0
        row = 39
        print("testcase004增加的邮箱格式不正确：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(9999, result['code'])
        print("code返回值：9999")

        self.assertEqual('Time out.', result['msg'])
        print("msg返回值：Time out.")

if __name__ == '__main__':
    unittest.main()

