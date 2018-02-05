import unittest,time,sys

from PIL import Image
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from testcase.models.function import Function

sys.path.append("../DATA")
from data_info import heaven_info

from login import TestLogin
from get_url import Url
from get_img import Img



class Test_personalorder():
    def setUp(self):
        time.sleep(2)


    def testpersonal_order(self,driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn):
        # 确定我已满18岁
        driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)

        # -------用户登录------
        TestLogin().testlogin(driver,An,Bn)
        time.sleep(3)
        try:
            #-----------------------点个人中心------------------------------
            driver.find_element_by_xpath("html/body/header/div/div[2]/div[3]/div[1]").click()
            time.sleep(4)

            #检查我的账户页面是否显示关键字Hello, heyu1229
            personal = driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div[2]/div[1]/span").text
            try:
                assert personal == "Hello, heyu1229"
                print("进入我的账户页面成功")
            except AssertionError as e:
                print("进入我的账户页面失败")

            time.sleep(2)
            #------------------------orders订单页面---------------------------
            driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]/div/dl[1]/dd[1]/a").click()
            time.sleep(4)
            #检查order页面是否显示关键字Orders
            orders = driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div[1]").text

            assert orders == "Orders"
            print("进入order页面成功")




        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(driver)
            raise
        time.sleep(2)