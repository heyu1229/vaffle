# -*- coding:UTF-8 -*-
from PIL import Image
from selenium import webdriver
import sys, unittest, time

sys.path.append("../DATA")
from data_info import heaven_info

sys.path.append("../UI")
from purchase import Testpurchase
from get_url import Url
from get_img import Img
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains



# ------------------------首页-Categories分类导航--Accessory--Drip Tip--------------------------------------------
class MyTest_HomePage_categories(unittest.TestCase):
    def setUp(self):
        time.sleep(2)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=socks5://172.100.10.6:1080')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        '''
        binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver = webdriver.Chrome()
        '''


        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    # ----------------------------首页-Categories分类导航--Accessory--Drip Tip检查----------------------------------------
    def test_homepage1(self, submenu=None):
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")
        An, Bn, Cn, Dn, En, Fn, Gn, Hn = heaven_info().userinfo_01()

        # 确定我已满18岁
        self.driver.find_element_by_xpath("html/body/div[8]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)

        try:
            # 鼠标悬停Categories

            move_mouse = self.driver.find_element_by_xpath("html/body/header/div[1]/div[3]/div[1]/div")
            ActionChains(self.driver).move_to_element(move_mouse).perform()
            time.sleep(3)

            # 鼠标悬停Accessory
            move_mouse = self.driver.find_element_by_xpath("html/body/header/div[1]/div[3]/div[1]/ul/li[6]/a")
            ActionChains(self.driver).move_to_element(move_mouse).perform()
            time.sleep(3)

            # 点Drip Tip
            self.driver.find_element_by_xpath("html/body/header/div[1]/div[3]/div[2]/div[6]/div[1]/div[1]/a").click()
            time.sleep(3)

            # 进入面包屑Drip Tip商品列表
            floor = self.driver.find_element_by_xpath("html/body/div[2]/div/main/div[1]/div[3]/span").text

            # 检查是否显示面包屑Drip Tip
            try:
                assert floor == "Drip Tips"
                print("进入分类导航的商品列表页面成功")
            except AssertionError as e:
                print("进入分类导航的商品列表页面失败")



        except Exception as msg:
            print(u"异常原因%s" % msg)
            # 图片名称加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            test_errorimage = Img().test_errorimage()
            self.driver.get_screenshot_as_file(test_errorimage+'error_%s.jpg' % nowTime)
            raise

        time.sleep(4)


if __name__ == '__main__':
    unittest.main()
