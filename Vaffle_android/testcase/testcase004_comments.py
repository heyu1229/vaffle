import os
import unittest,time
from appium import webdriver
from public.installapp import androidtest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class AndroidTest_comments(unittest.TestCase):

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
    #-----------------------给POST评论---------------------------------------------
    def testcase001_post_coomments(self):
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
        #给第一个POST评论
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/item_post_comment').click()
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/ed_comment').send_keys("This is an auto comment.") #输入评论内容
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/btn_send' ).click() #提交评论成功
        self.public.swipeDown(1000)
        #断言是否评论成功
        comment_context = self.driver.find_element_by_id('com.heavengifts.vaffle:id/tv_main_content').text
        # self.assertEqual ( comment_context, 'This is an auto comment.')
        self.assertEqual ( comment_context, 'This is an auto comment.', self.write.Write_data ( 1, 14, 4, '评论失败' ) )
        self.write.Write_data ( 1, 14, 4, '评论成功' )


    def tearDown(self):
        os.system ( 'start stopAppiumServer.bat' )
        time.sleep(20)
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()