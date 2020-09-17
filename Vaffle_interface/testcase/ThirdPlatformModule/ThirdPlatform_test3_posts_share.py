# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------第三方分享回调接口----------------------
from Vaffle_interface.public_1.get_url import Url
from Vaffle_interface.public_1.sql_search import SQL_SEARCH_1
from Vaffle_interface.public_1.sql_vaffle import SQL_vaffle


class Post_share(unittest.TestCase):

    def setUp(self):
        self.requests = FuncRequests()
        self.member_uuid = Url().test_user()

    #-----------------第三方分享回调----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 3
        print("testcase_001第三方分享回调")

        sql = SQL_vaffle.select_post_id(self)
        post_id = SQL_SEARCH_1.search(sql)
        print(post_id)
        #
        # #调用第三方分享回调接口
        payload = {'platform':'facebook','post_id':post_id}
        result=self.requests.interface_requests_payload(self.member_uuid, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


if __name__=="__main__":
    unittest.main()
