# -*- coding:UTF-8 -*-
from UI.get_url import Url
import sys,unittest,time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from testcase.models.function import Function
from testcase.models.myunit import MyTest

sys.path.append("../DATA")
from data_info import heaven_info
sys.path.append("../UI")
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#------------------------检查是否通过quick view加入购物车页面------------------------------------------
class MyTest_Quick_cart(unittest.TestCase):

    def test_quick_cart(self):
        self.driver = MyTest().setUp()
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")
        An,Bn,Cn,Dn,En,Fn,Gn,Hn = heaven_info().userinfo_01()

        # 确定我已满18岁
        self.driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)
        # ----------------------首页-----------------------------
        # 搜索商品名称
        self.driver.find_element_by_id ( "kw" ).send_keys ( Cn )
        time.sleep ( 3 )
        # 点search按钮
        self.driver.find_element_by_id ( "searchTextBtn" ).click ()
        time.sleep ( 6 )
        try:
            # 鼠标悬停

            move_mouse = self.driver.find_element_by_xpath("html/body/div[3]/div/main/section[1]/ul/li[1]/div")
            ActionChains(self.driver).move_to_element(move_mouse).perform()
            time.sleep(2)

            #点击第一个商品quick cart按钮，弹框
            self.driver.find_element_by_xpath("html/body/div[3]/div/main/section[1]/ul/li[1]/div/div[3]").click()
            time.sleep(8)

            #选择Color--blue
            # sel = Select(self.driver.find_element_by_name ( "productId" )) # 实例化Select
            # sel.select_by_visible_text ( 'Blue' )
            self.driver.find_element_by_xpath ("html/body/div[16]/div/div/div/div/div/div[1]/div[5]/dl/div[2]/dd/select" ).click ()
            time.sleep(2)
            self.driver.find_element_by_xpath ( "html/body/div[16]/div/div/div/div/div/div[1]/div[5]/dl/div[2]/dd/select/option[2]" ).click ()
            time.sleep(2)
            #点击 Add to Cart按钮
            self.driver.find_element_by_xpath ( "html/body/div[16]/div/div/div/div/div/div[1]/div[6]/button[1]" ).click()
            time.sleep(4)
            #关闭弹框
            self.driver.find_element_by_xpath ("html/body/div[16]/div/a" ).click ()
            time.sleep(2)

            #点击Cart进入购物车
            self.driver.find_element_by_xpath ( "html/body/header/div/div[2]/div[3]/div[2]" ).click ()
            time.sleep(4)
            goods = self.driver.find_element_by_xpath ( "html/body/div[3]/div[4]/div[2]/form/div/table/tbody/tr/td[2]/p[1]/a" ).text
            print(goods)
            #检查商品是否已加入购物车
            # try:
            assert goods == "GeekVape Medusa Reborn RDTA 3.5ml"
            print("quick加入购物车成功")
            # except AssertionError as e:
            #     print("quick加入购物车失败")

        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(self.driver)
            raise

        time.sleep(4)
        MyTest().tearDown(self.driver)





if __name__ == '__main__':
    unittest.main()

