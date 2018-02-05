# -*- coding:UTF-8 -*-
import sys,unittest,time

from UI.get_img import Img
from pyse import TestCase, TestRunner
from testcase.models.function import Function
from testcase.models.myunit import MyTest

sys.path.append("../DATA")
from data_info import heaven_info
sys.path.append("../UI")
from get_url import Url
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# noinspection PyUnresolvedReferences
from PIL import Image

#------------------------首页搜索商品------------------------------------------
class MyTest_HomePage_Search(TestCase):
    def test_homepage_search(self):
        try:
            url = Url().test_url()
            self.base_url = url+"/"
            self.driver.open ( self.base_url )
            An,Bn,Cn,Dn,En,Fn,Gn,Hn = heaven_info().userinfo_01()

            # 确定我已满18岁
            # self.driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
            self.driver.click ( "xpath=>html/body/div[9]/div/div/div/div/div/div[2]/button[2]" )
            time.sleep(2)
            # -------搜索商品进入商品列表页------------
            self.driver.type ( "id=>kw", Cn )
            self.driver.click ( "id=>searchTextBtn" )
            # 检验是否成功进入搜索商品列表
            self.assertTitle ( "[Pre-order] GeekVape Medusa Reborn RDTA - 3.5ml -" )
        except Exception as msg:
            print(u"异常原因%s" % msg)
            nowTime = time.strftime ( "%Y%m%d.%H.%M.%S" )
            test_errorimage = Img ().test_errorimage ()
            self.driver.get_windows_img( test_errorimage + 'error_%s.png' % nowTime )
            raise

        time.sleep(5)
        MyTest().tearDown(self.driver)

if __name__ == '__main__':
    unittest.main()
    runner = TestRunner('./','首页搜索商品','正式环境：Chrome')
    runner.run()

