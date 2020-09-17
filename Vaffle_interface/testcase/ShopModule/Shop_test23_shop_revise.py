# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------管理我的店铺 - 店铺主页修改----------------------
class Shop(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------管理我的店铺 - 店铺主页修改----------------------------------
    def testcase_001(self):
        sheet_index = 12
        row = 28
        member_id='7238fc91-0b5e-4f14-8288-95f60dae7658'
        print ("testcase_001管理我的店铺 - 店铺主页修改:")

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        obj=[{"week":["1","2","3","4","5","6","7"],"start":"09:00","close":"18:00"},]
        business_hours=json.dumps(obj)
        payload = {"name": "Queenstore test 001", "info": "info","cover":"posts/1512710644871_767_android.jpg","business_hours":business_hours,
                   "tel":"15800328065","nation":"China","city":"shanghai","address":"qilianshanlu","payment":"zhifubao",
                   "ins":"www.ins.com","youtube":"www.youtube.com","twitter":"www.twitter.com","website":"www.baidu.com",
                   "facebook":"www.fb1.com","shop_id":"54273","timezone":8,"normal_member_uuid":'b9f73f23-7bc6-4de6-9f9b-df2c98076221',
                   "is_delivery":1}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()