# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------发送帖子信息至聊天页---------------------
class Message(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------发送帖子信息至聊天页---------------------------------
    def testcase_001(self):
        sheet_index = 5
        row = 19
        print("testcase_001 发送帖子信息至聊天页：")

        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        payload = {'post_id':98743,'type':'person','to_id':'test_963','category':'posts','nickname':'queen','content':'Rutiti',
                   'postType':2,'ratio':'1.23','image':"https://duly5zwcucles.cloudfront.net/middle/posts/159728401040028_99b0b05d7ff8541ad723318c3693034f_ios.jpg"}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()