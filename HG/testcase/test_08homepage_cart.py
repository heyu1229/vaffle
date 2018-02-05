# -*- coding:UTF-8 -*-
import sys,unittest,time
from testcase.models.function import Function
from testcase.models.myunit import MyTest

sys.path.append("../DATA")
from data_info import heaven_info
sys.path.append("../UI")
from get_url import Url
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#------------------------检查是否成功进入购物车页面------------------------------------------
class MyTest_HomePage_cart(unittest.TestCase):

    def test_homepage_cart(self):
        self.driver = MyTest().setUp()
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")
        An,Bn,Cn,Dn,En,Fn,Gn,Hn = heaven_info().userinfo_01()

        # 确定我已满18岁
        self.driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)

        try:
            #点cart
            self.driver.find_element_by_xpath("html/body/header/div/div[2]/div[3]/div[2]").click()
            time.sleep(4)

            time.sleep(2)
            #检查是否显示关键字1.View Shopping Cart
            cart = self.driver.find_element_by_xpath("html/body/div[3]/div[3]/span[1]").text
            assert cart == "1.View Shopping Cart"
            print("进入cart页面成功")




        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(self.driver)
            raise

        time.sleep(4)
        MyTest().tearDown(self.driver)




if __name__ == '__main__':
    unittest.main()

