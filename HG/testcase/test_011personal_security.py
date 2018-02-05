# -*- coding:UTF-8 -*-
import sys,unittest,time

from testcase.models.myunit import MyTest

sys.path.append("../DATA")
from data_info import heaven_info
sys.path.append("../UI")
from personal_security import Test_personalsecurity

from get_url import Url
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#------------------------检查是否成功进入修改密码页面------------------------------------------
class MyTest_Personal_security(unittest.TestCase):

    def test_personal_security(self):
        self.driver = MyTest().setUp()
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")
        An,Bn,Cn,Dn,En,Fn,Gn,Hn = heaven_info().userinfo_01()
        time.sleep(2)
        Test_personalsecurity().testpersonal_security(self.driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn)
        MyTest().tearDown(self.driver)



if __name__ == '__main__':
    unittest.main()

