# -*- coding:UTF-8 -*-
import unittest,time,sys


sys.path.append("../DATA")
from data_info import heaven_info


# -------------------登录-----------------------------
class TestLogin(unittest.TestCase):
    def setUp(self):
        time.sleep(2)

    def testlogin(self,driver,An,Bn):

        # 登录
        driver.find_element_by_xpath("html/body/header/div[3]/div/div[4]/div[2]/div[1]/span[2]/em[1]/a[1]").click()
        time.sleep(3)
        # -------------------进入登录页面-------------------------------------------
        # 用户名
        driver.find_element_by_name("login_name").send_keys(An)
        # inputTest = "$(':text').val('aaaa')"
        # driver.execute_script ( inputTest )
        # 密码
        driver.find_element_by_name("password_shadow").send_keys(Bn)
        time.sleep(1)
        # 登录
        driver.find_element_by_id("login_submit").click()
        # inputTest = "$('#login_submit').click()"
        # driver.execute_script ( inputTest )
        time.sleep(1)
