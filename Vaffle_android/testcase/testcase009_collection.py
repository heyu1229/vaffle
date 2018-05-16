import os
import unittest,time
from appium import webdriver
from public.installapp import androidtest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class AndroidTest_likes(unittest.TestCase):

    def setUp(self):
        # os.system ( 'start startAppiumServer.bat' )
        time.sleep ( 10 )
        Android = androidtest()
        self.driver=Android.android()
        self.public=Publicway(self.driver)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 1, 0)
        self.password = int(self.read.Read_data(0, 1, 1))
    #-----------------------收藏POST---------------------------------------------
    def testcase001_post_likes(self):
        print(self.user, self.password)
        #登录用户
        self.public.login_vaffle(self.user, self.password)
        #-------------------------------新发一条纯文本POST------------------------------------------
        # 点击发布按钮
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
        self.public.swipeDown(2000)
        time.sleep(5)
        #收藏第一个POST
        posts = self.driver.find_elements_by_id('com.heavengifts.vaffle:id/home_recyclerview')
        onepost = posts[0].find_element_by_id('com.heavengifts.vaffle:id/post_image_item')
        onepost.find_element_by_id('com.heavengifts.vaffle:id/item_post_collect').click()
        time.sleep(2)
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/bottom_menu_me' ).click () #进入我的页面
        # 进入Collection页面
        me = self.driver.find_element_by_id('com.heavengifts.vaffle:id/home_recyclerview')
        menus = me.find_elements_by_id('com.heavengifts.vaffle:id/me_account_layout')
        menus[1].find_element_by_id('com.heavengifts.vaffle:id/tv_set_item_name').click()

        #定位收藏的第一个Post内容
        collection = self.driver.find_element_by_id('com.heavengifts.vaffle:id/home_recyclerview')
        posts = collection.find_elements_by_id('com.heavengifts.vaffle:id/post_image_item')
        text = posts[0].find_element_by_id('com.heavengifts.vaffle:id/item_post_content').text

        #断言是否收藏成功
        # self.assertEqual ( nickname, '@'+self.user )
        self.assertEqual ( text, date+' auto test post text', self.write.Write_data ( 1, 16, 4, '收藏失败' ) )
        self.write.Write_data ( 1, 16, 4, '收藏成功' )


    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat' )
        time.sleep(200)
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()