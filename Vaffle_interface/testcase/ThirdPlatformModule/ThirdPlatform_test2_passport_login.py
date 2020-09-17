# -*- coding:UTF-8 -*-
import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------第三方登录接口----------------------
class Passport_Login(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------第三方facebook登录成功----------------------------------
    #-----------------facebook:411568645883504 twitter:861855853032357889  vk:427871220--------------------------
    def testcase_001(self):
        sheet_index = 6
        row = 2
        print("testcase_001第三方facebook登录成功：")
        data = int(time.time())
        member_id = "none"
        payload = {'platform':'facebook','open_id':'587211848358211','nickname':'Luo_Taibin898',
                   'gender':'N','equipment_number':'1589345731','email':'facebook@email'+str(data)+'.com'}
        result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")




if __name__=="__main__":
    unittest.main()
