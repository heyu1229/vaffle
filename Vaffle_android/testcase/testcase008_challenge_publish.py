import os
import unittest,time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from public.installapp import androidtest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

#-------------------发布挑战活动的post-----------------------------------------
class AndroidTest_challenge_publish(unittest.TestCase):

    def setUp(self):
        os.system ( 'start startAppiumServer.bat' )
        time.sleep ( 10 )
        Android = androidtest()
        self.driver=Android.android()
        self.public=Publicway(self.driver)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 1, 0)
        self.password = int(self.read.Read_data(0, 1, 1))
    #-----------------------发布挑战活动的post--------------------------------------------
    def testcase001_post_text(self):
        print(self.user, self.password)
        #登录用户
        self.public.login_vaffle(self.user, self.password)
        #进入discover页面
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_discover').click()
        #进入第一个活动挑战页面
        discover = self.driver.find_element_by_id('com.heavengifts.vaffle:id/home_recyclerview')
        challenges = discover.find_elements_by_id('com.heavengifts.vaffle:id/ll_challenge')
        challenges[1].find_element_by_id('com.heavengifts.vaffle:id/tv_people_num').click()
        #活动挑战页面点Enter
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/tv_join').click()
        try:
            if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
                #点允许直接进入相册页面
                self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        except:
            print("no alter")

        #选择第一张照片后发布活动Post
        library = self.driver.find_element_by_id("com.heavengifts.vaffle:id/library_grid")
        photoes = library.find_elements_by_class_name('android.widget.FrameLayout')
        photoes[1].click()#选择第一张照片
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/iv_select").click() #打勾
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/share_to_et').send_keys(date + ' auto test challenge post') #输入纯文本
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_toolbar_right').click()  #提交发布
        # 返回discover页面
        toolbar = self.driver.find_element_by_id('com.heavengifts.vaffle:id/toolbar')
        toolbar.find_element_by_class_name('android.widget.ImageButton').click()
        time.sleep(10)
        # self.public.swipeDown(5)
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_me').click()  #进入Me页面
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/cnt_posts').click() #进入POSTS页面
        text = self.driver.find_element_by_id('com.heavengifts.vaffle:id/item_post_content').text
        print(text)
        self.assertEqual(text, date + ' auto test challenge post',self.write.Write_data(1,8,4,'发布失败'))
        self.write.Write_data(1,8,4,'发布成功')

    def tearDown(self):
        os.system ( 'start stopAppiumServer.bat' )
        time.sleep(20)
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()