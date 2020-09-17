# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------产品 - 删除产品----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------产品 - 删除一个产品----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 33
        member_id='7238fc91-0b5e-4f14-8288-95f60dae7658'
        print ("testcase_001删除一个产品:")

        # 调用新增产品接口发送一条动态，获取product_ids
        product_ids = product()

        payload={ "shop_id": 54273, "normal_member_uuid": 'b9f73f23-7bc6-4de6-9f9b-df2c98076221',
                  "product_ids":product_ids}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()


def product():
    # 调用新增产品接口发送一条动态，获取product_ids
    r = FuncRequests()
    for index in range(0, 1):
        member_id = '7238fc91-0b5e-4f14-8288-95f60dae7658'
        obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
        images = json.dumps(obj)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload1 = {"name": "autotest" + date, "description": "description" + date, "total": 3, "images": images,
                   "shop_id": 54273, "normal_member_uuid": 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'}

        urlpart1 = '/product/add'
        result1 = r.interface_requests_data(member_id, urlpart1, payload1)
        product_id = result1["data"]["product_id"]
        print('product_id=',product_id)
        return product_id