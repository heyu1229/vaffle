# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------[webapi]post点赞记录列表----------------------
class web_posts_praiserecord(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------[webapi]post点赞记录列表----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 53
        print("testcase_001 post点赞记录列表：")

        member_id = "b9f73f23-7bc6-4de6-9f9b-df2c98076221"
        tik = "WmhISnZ1aHROSXg0Z21ybVBOR3BuNGx0TU1ZcnJ0MFcyQ2FXaGRra3h0c3V6RVduOGppbnUwNTA2RENKS0VmM3ZpMGxaK3VMY2VkclQ3dGJ1bG1ORjhLZmVEc0NXTTUyaUtlWlJHL0Vac1BSenNkY2xVZ3V2b0tWQTNqMjFWMm0weHVpVGpxOFMwUXpPSGszdDVDSzZhc08zTUZjL3Roak1TY3BhZGNGZ2RnPQ"
        payload = {}
        result = self.r.interface_requests_payload_tik(member_id, sheet_index, row, payload,tik)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()