# -*- coding:UTF-8 -*-
import sys,unittest,time

from testcase.models.myunit import MyTest

sys.path.append("../DATA")
from data_info import heaven_info
sys.path.append("../UI")
from personal_order import Test_personalorder
from get_url import Url
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#------------------------检查是否成功进入个人中心页面及订单页面------------------------------------------
class MyTest_Personal_order(unittest.TestCase):

    def test_personal_order(self):
        self.driver = MyTest().setUp()
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")
        An,Bn,Cn,Dn,En,Fn,Gn,Hn = heaven_info().userinfo_01()
        time.sleep(2)
        Test_personalorder().testpersonal_order(self.driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn)
        MyTest().tearDown(self.driver)



if __name__ == '__main__':
    unittest.main()

