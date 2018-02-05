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
        An,Bn,Cn,Dn,En,Fn,Gn,Hn = heaven_info().userinfo_01()
        print("用户名：%s"%An)
        print("密码：%s"%Bn)
        print("商品名称：%s"%Cn)
        print("商品数量：%s"%Dn)
        print("送货方式：%s"%En)
        print("支付方式：%s"%Fn)
        print("下单留言内容：%s"%Gn)
        print("下单1付款2 不付款直接到商品详情页：%s"%Hn)
        Testpurchase().testpurchase(self.driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn)
        MyTest().tearDown(self.driver)





if __name__ == '__main__':
    unittest.main()

