# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------相册内图片删除----------------------
class Group_noticedel(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------相册内图片删除--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 54
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 相册内图片删除:")

        payload1 = {'album_id': 201,'page':1}
        urlpart1 = '/group/album/picture/lists'
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        photo_id = result1['data']['list'][0]['id']

        p = []
        p.append(photo_id)
        p = tuple(p)
        id = json.dumps(p)
        print('photo_id=', id)
        payload = {'photo_id':id,'guid':'48afaa46-0d80-4518-a880-3577530440d0'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()