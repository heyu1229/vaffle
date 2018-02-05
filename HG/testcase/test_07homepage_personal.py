# -*- coding:UTF-8 -*-
from PIL import Image
from selenium import webdriver
import sys,unittest,time

from testcase.models.function import Function
from testcase.models.myunit import MyTest

sys.path.append("../DATA")
from data_info import heaven_info
sys.path.append("../UI")
from purchase import Testpurchase
from get_url import Url
from get_img import Img
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#------------------------检查是否成功进入登录/个人中心页面------------------------------------------
class MyTest_HomePage_personal(unittest.TestCase):

    def test_homepage_personal(self):
        self.driver = MyTest().setUp()
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")
        # 确定我已满18岁
        self.driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)

        try:
            #点个人中心
            self.driver.find_element_by_xpath("html/body/header/div/div[2]/div[3]/div[1]").click()
            time.sleep(4)

            time.sleep(2)
            #检查是否显示关键字Welcome to login
            personal = self.driver.find_element_by_xpath("html/body/div[3]/div/div/form/div[1]/div[1]/h3").text

            assert personal == "Welcome to login"
            print("进入登录页面成功")




        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(self.driver)
            raise

        time.sleep(4)
        MyTest().tearDown(self.driver)





if __name__ == '__main__':
    unittest.main()

