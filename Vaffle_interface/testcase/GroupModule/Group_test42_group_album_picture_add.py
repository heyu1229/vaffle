# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


#---------------相册图片添加----------------------
class Group_noticedel(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------相册图片添加--------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 53
        member_id='b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print ("testcase_001 相册图片添加:")

        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        payload = {'album_id':201,'images':images}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()