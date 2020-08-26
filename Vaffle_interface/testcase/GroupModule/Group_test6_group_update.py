# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------更新群组信息----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------更新群组信息---------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 6
        member_id = 'b9f73f23-7bc6-4de6-9f9b-df2c98076221'
        print("testcase_001 更新群组信息:")
        obj = ({"icon" : "https:\/\/duly5zwcucles.cloudfront.net\/icon\/group_facebook_ga.png","k" : "facebook","v" : ""},
               {"icon" : "https:\/\/duly5zwcucles.cloudfront.net\/icon\/group_twitter_ga.png","k" : "twitter","v" : ""},
               {"icon" : "https:\/\/duly5zwcucles.cloudfront.net\/icon\/group_vk_ga.png","k" : "vk","v" : ""},
               {"v" : "","icon" : "https:\/\/duly5zwcucles.cloudfront.net\/icon\/group_instagram_ga_new.png","k" : "instagram"},)
        media = json.dumps(obj)
        payload = {"title": "uuu", "guid": "48afaa46-0d80-4518-a880-3577530440d0","media":media,"group_description":"group_description",
                   "address":"来登饭店"}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()