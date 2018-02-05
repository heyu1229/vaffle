# -*- coding:UTF-8 -*-
import sys,unittest,time

from testcase.models.function import Function
from testcase.models.myunit import MyTest

sys.path.append("../DATA")
sys.path.append("../UI")
from get_url import Url
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#------------------------new arrival楼层more检查------------------------------------------
class MyTest_HomePage_floormore(unittest.TestCase):

    #----------------------------new arrival楼层more检查----------------------------------------
    def test_homepage_floormore(self):
        self.driver = MyTest().setUp()
        url = Url().test_url()
        self.base_url = url
        self.driver.get(self.base_url + "/")

        # 确定我已满18岁
        self.driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)

        # 将页面滚动条拖到下一页
        js = "var q=document.body.scrollTop=500"
        self.driver.execute_script(js)
        time.sleep(2)

        try:
            #点New Arrival   view more
            self.driver.find_element_by_xpath("html/body/div[3]/main/div[2]/section[1]/a").click()
            time.sleep(4)

            floor = self.driver.find_element_by_xpath("html/body/div[3]/div/main/div[1]/div[2]/span").text
            print(floor)

            time.sleep(2)
            #检查是否显示关键字New Arrival

            assert floor == "New Arrival"
            print("进入New Arrival更多商品列表页成功")



        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(self.driver)
            raise

        time.sleep(4)
        MyTest().tearDown(self.driver)




if __name__ == '__main__':
    unittest.main()

