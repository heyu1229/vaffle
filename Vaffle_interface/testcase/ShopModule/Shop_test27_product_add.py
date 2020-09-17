# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------产品 - 新增 产品----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------产品 - 新增 产品----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 32
        member_id='7238fc91-0b5e-4f14-8288-95f60dae7658'
        print ("testcase_001新增产品:")

        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        print("images=",images)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {"name": "autotest"+date,"description":"description"+date, "total": 3,"images": images,
                   "shop_id":54273,"normal_member_uuid":'b9f73f23-7bc6-4de6-9f9b-df2c98076221'}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        product_id = result["data"]["product_id"]
        print('product_id=', product_id)

        urlpart1 = '/product/delete'
        payload1 = {"shop_id": 54273, "normal_member_uuid": 'b9f73f23-7bc6-4de6-9f9b-df2c98076221',
                   "product_ids": product_id}
        result1 = self.r.interface_requests_data(member_id, urlpart1, payload1)
        print(result1['code'])

if __name__ == "__main__":
    unittest.main()