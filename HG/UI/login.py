# -*- coding:UTF-8 -*-
import unittest,time,sys


sys.path.append("../DATA")
from data_info import heaven_info




class TestLogin(unittest.TestCase):
    def setUp(self):
        time.sleep(2)

    def testlogin(self,driver,An,Bn):

        # 登录
        #driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div[2]/a[1]").click()
        driver.find_element_by_xpath("html/body/header/div/div[2]/div[3]/div[1]").click()
        #driver.find_element_by_class_name("min_my_account has_pop").click
        time.sleep(6)
        # -------------------进入登录页面-------------------------------------------
        # 用户名
        driver.find_element_by_id("login_name").send_keys(An)
        # 密码
        driver.find_element_by_id("password_shadow").send_keys(Bn)
        time.sleep(1)
        # 万能验证码
        driver.find_element_by_id("verifyCode").send_keys("wnyz")
        time.sleep(1)
        # 登录
        driver.find_element_by_id("login_submit").click()
        time.sleep(1)
