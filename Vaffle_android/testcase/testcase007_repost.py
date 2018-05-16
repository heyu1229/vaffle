import os
import unittest,time
from appium import webdriver
from public.installapp import androidtest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class AndroidTest_repost(unittest.TestCase):

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
    #-----------------------转发POST---------------------------------------------
    def testcase001_repost(self):
        print(self.user, self.password)
        #登录用户
        self.public.login_vaffle(self.user, self.password)
        #点击发布按钮
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_publish').click()
        try:
            if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
                #点允许直接进入相册页面
                self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        except:
            print("no alter")

        #选择第一张照片后删除,再输入纯文本
        library = self.driver.find_element_by_id("com.heavengifts.vaffle:id/library_grid")
        photoes = library.find_elements_by_class_name('android.widget.FrameLayout')
        photoes[1].click()#选择第一张照片
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/iv_select").click() #打勾
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/img_pix_delete").click() #删除已选图片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/share_to_et').send_keys(date + ' auto test post text') #输入纯文本
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_toolbar_right').click()
        time.sleep(5)
        self.public.swipeDown(2000)

        home = self.driver.find_element_by_id("com.heavengifts.vaffle:id/home_recyclerview")
        posts = home.find_elements_by_id("com.heavengifts.vaffle:id/post_image_item")
        posts[0].find_element_by_id("com.heavengifts.vaffle:id/item_post_foword").click()
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/share_to_et' ).send_keys (
            date + ' This is a repost.' )  # 输入转发文本
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/push_display").click()

        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_me').click()  #进入Me页面
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/cnt_posts').click() #进入POSTS页面
        text = self.driver.find_element_by_id('com.heavengifts.vaffle:id/item_post_content').text
        print(text)
        self.assertEqual(text, date + ' This is a repost.',self.write.Write_data(1,10,4,'转发失败'))
        self.write.Write_data(1,10,4,'转发成功')
        time.sleep(2)
        

    def tearDown(self):
        os.system ( 'start stopAppiumServer.bat' )
        time.sleep(20)
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()