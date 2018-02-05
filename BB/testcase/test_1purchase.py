# -*- coding:UTF-8 -*-
import sys,unittest,time

from testcase.models.myunit import MyTest
sys.path.append("../DATA")
from data_info import heaven_info
sys.path.append("../UI")
from purchase import Testpurchase
from get_url import Url
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class MyTest_purchase(unittest.TestCase):

    def test_purchase(self):
        self.driver = MyTest().setUp()
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")
        An,Bn,Cn,Dn,En,Fn,Gn,Hn,In,Jn = heaven_info().userinfo_01()
        print("用户名：%s"%An)
        print("密码：%s"%Bn)
        Testpurchase().testpurchase(self.driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn,In,Jn)
        MyTest().tearDown(self.driver)





if __name__ == '__main__':
    unittest.main()

