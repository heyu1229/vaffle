# -*- coding:UTF-8 -*-
from PIL import Image
from selenium import webdriver
import sys,unittest,time
sys.path.append("../DATA")
from data_info import heaven_info
sys.path.append("../UI")
from purchase import Testpurchase
from get_url import Url
from get_img import Img
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#------------------------new arrival楼层商品详情检查------------------------------------------
class MyTest_HomePage_floor(unittest.TestCase):

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

    #----------------------------new arrival楼层第一个商品详情检查----------------------------------------
    def test_homepage1(self):
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")
        An,Bn,Cn,Dn,En,Fn,Gn,Hn = heaven_info().userinfo_01()

        # 确定我已满18岁
        self.driver.find_element_by_xpath("html/body/div[8]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)

        # 将页面滚动条拖到下一页
        js = "var q=document.body.scrollTop=1000"
        self.driver.execute_script(js)
        time.sleep(2)

        try:
            # 鼠标悬停Best Seller楼层第1个商品
            move_mouse = self.driver.find_element_by_xpath("html/body/div[2]/main/div[2]/section[2]/ul/li[1]/div")
            ActionChains(self.driver).move_to_element(move_mouse).perform()
            time.sleep(5)

            #选择color
            #self.driver.find_element_by_name("productId").find_elements_by_tag_name("option")[1].click()
            self.driver.find_element_by_xpath ("html/body/div[2]/main/div[2]/section[2]/ul/li[1]/div/div[2]/div/select" ).click ()
            time.sleep(2)
            self.driver.find_element_by_xpath ("html/body/div[2]/main/div[2]/section[2]/ul/li[1]/div/div[2]/div/select/option[2]" ).click ()
            time.sleep(2)
            #加入购物车
            self.driver.find_element_by_xpath("html/body/div[2]/main/div[2]/section[2]/ul/li[1]/div/div[2]/button[1]").click()
            time.sleep(3)

            # 将页面滚动条拖到顶部
            js = "var q=document.body.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(3)

            #点击购物车
            self.driver.find_element_by_xpath("html/body/header/div/div[2]/div[3]/div[2]").click()

            time.sleep(3)
            title = self.driver.find_element_by_xpath("html/body/div[2]/div[4]/div[2]/form/table/tbody/tr/td[2]/p[1]/a").text
            print("new arrival楼层第一个商品标题：%s"%title)




        except Exception as msg:
            print(u"异常原因%s" % msg)
            # 图片名称加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            test_errorimage = Img().test_errorimage()
            self.driver.get_screenshot_as_file(test_errorimage+'error_%s.jpg' % nowTime)
            raise

        '''
        #检验是否成功进入商品详情页
        try:
            assert title == self.driver.find_element_by_xpath("html/body/div[2]/div[2]/div[1]/div[2]/div[2]/h1/span").text
            print("进入商品详情页成功")
        except AssertionError as e:
            print("进入商品详情页失败")
        '''
        time.sleep(2)





if __name__ == '__main__':
    unittest.main()

