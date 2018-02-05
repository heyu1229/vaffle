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



class Test_personalsecurity():
    def setUp(self):
        time.sleep(2)


    def testpersonal_security(self,driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn):
        # 确定我已满18岁
        driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)

        # -------用户登录------
        TestLogin().testlogin(driver,An,Bn)
        time.sleep(3)
        #-----------------------点个人中心------------------------------
        driver.find_element_by_xpath("html/body/header/div/div[2]/div[3]/div[1]").click()
        time.sleep(4)
        try:
            #------------------------点security修改密码---------------------------
            driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]/div/dl[4]/dd[2]/a").click()
            time.sleep(4)
            #检查是否成功进入密码修改页面

            assert driver.find_element_by_xpath("html/body/div[3]/div[2]/form/div/div[1]").text == "Security"
            print("成功进入密码修改页面")




        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(driver)
            raise
        time.sleep(5)