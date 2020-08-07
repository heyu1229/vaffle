# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------[webapi] post、reveal首页动态列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------[webapi] post首页动态列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 50
        print("testcase_001 post首页动态列表：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        payload = {"type":"post","page":1}
        tik = "WmhISnZ1aHROSXg0Z21ybVBOR3BuNGx0TU1ZcnJ0MFcyQ2FXaGRra3h0c3V6RVduOGppbnUwNTA2RENKS0VmM3ZpMGxaK3VMY2VkclQ3dGJ1bG1ORjhLZmVEc0NXTTUyaUtlWlJHL0Vac1BSenNkY2xVZ3V2b0tWQTNqMjFWMm0weHVpVGpxOFMwUXpPSGszdDVDSzZhc08zTUZjL3Roak1TY3BhZGNGZ2RnPQ"
        result = self.r.interface_requests_payload_tik(member_id, sheet_index, row, payload,tik)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()