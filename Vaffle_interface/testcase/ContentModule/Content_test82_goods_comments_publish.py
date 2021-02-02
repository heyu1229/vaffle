# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------问题删除功能---------------------
from Vaffle_interface.public_1.func_requests import FuncRequests
from Vaffle_interface.public_1.get_url import Url

#-----------------商品评价-----------
class Question_edit(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()
        self.member_uuid = Url().test_user()

    def testcase_001(self):
        sheet_index = 1
        row = 102

        obj = ({"path": "posts/1512710644881_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {'content': date+'发布商品评价','images':images,'score':8,'goods_id':1}
        result = self.r.interface_requests_payload(self.member_uuid, sheet_index, row, payload)
        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()