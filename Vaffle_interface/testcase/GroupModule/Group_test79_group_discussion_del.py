# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#------------------群组讨论删除----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #----------------------群组讨论删除------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 91
        print("testcase_001 群组讨论删除:")

        #发布一个话题
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        data = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        payload1 = {'guid':'48afaa46-0d80-4518-a880-3577530440d0','title':'del'+data,'topic_content':'test to del'}
        urlpart1 = '/group/topic/public'
        result1 = self.r.interface_requests_data(member_id,urlpart1,payload1)
        topic_id = result1['data']['topic_id']
        print('topic_id=',topic_id)

        payload = {'topic_id':topic_id}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()