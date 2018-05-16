import os
import unittest,time
from appium import webdriver
from public.installapp import androidtest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from public.findtoast import Findtoast



class AndroidTest_avatar(unittest.TestCase):

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


    # -----------------------新注册用户上传头像，头像为拍照图片---------------------------------------------
    def testcase001_upload_avatar(self):
        date = time.strftime('%H%M%S', time.localtime())
        displayname = "lisa"+date
        email = "lisa"+date+"@163.com"
        password ="111111"
        # 注册用户
        self.driver.implicitly_wait ( 10 )
        try:
            if self.driver.find_element_by_xpath ( "//*[@text='Updates']" ).is_displayed ():
                self.driver.find_element_by_xpath ( "//*[@text='Cancel']" ).click ()
        except:
            print ( "no update" )
        # self.driver.find_element_by_id("com.heavengifts.vaffle:id/update_cancel").click()

        # 点菜单进入登录页面
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/bottom_menu_me" ).click ()
        # 点右上角Sign Up按钮进入注册页面
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/menu_right" ).click ()
        # 输入name/e-mail/password

        names = self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/l_param1" )
        names.find_element_by_id ( "com.heavengifts.vaffle:id/ed_content" ).send_keys ( displayname )

        emails = self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/l_param2" )
        emails.find_element_by_id ( "com.heavengifts.vaffle:id/ed_content" ).send_keys ( email )

        passwords = self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/l_param3" )
        passwords.find_element_by_id ( "com.heavengifts.vaffle:id/ed_content" ).send_keys ( password )


        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/btn_sign_before" ).click ()
        # 进入注册2页面点Sign Up按钮  注册成功后进入首页
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/ct_certification").click()         #勾选我已满18周岁
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/btn_register" ).click ()
        # 进入Me页面
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/bottom_menu_me' ).click ()  # 点击我的
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/avatar' ).click ()  # 点击头像
        try:
            if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
                #点允许直接进入相册页面
                self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        except:
            print("no alter")
        # 拍照发POST
        library = self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/library_grid" )
        photoes = library.find_elements_by_class_name ( 'android.widget.FrameLayout' )
        photoes[0].click ()  # 拍照
        self.driver.find_element_by_id ('com.android.packageinstaller:id/permission_allow_button').click ()  # 允许访问相机或录制视频
        # self.driver.find_element_by_id ( 'com.android.packageinstaller:id/permission_allow_button' ).click ()  # 允许访问麦克风
        # except:
        #     print("no alter")
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/view_photo_video_select' ).click ()  # 点击拍照
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/view_operate_done' ).click ()  # 点击提交照片
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/menu_sava" ).click ()  # 裁剪，点Next
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/tv_done" ).click ()  # 点Done

    #-----------------------修改头像,且图片加滤镜---------------------------------------------
    def testcase002_avatar(self):
        print(self.user, self.password)
        #登录用户
        self.public.login_vaffle(self.user, self.password)
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_me').click() # 点击我的
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/avatar').click() # 点击头像
        try:
            if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
                #点允许直接进入相册页面
                self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        except:
            print("no alter")
        time.sleep(5)
        # self.driver.execute_script ( "mobile: tap", {"touchCount": "1", "x": 977, "y": 131} )
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/tv_edit').click()   #点击Edit
        # self.driver.find_element_by_xpath ( "//android.widget.TextView[contains(@text,'Edit')]" ).click ()   #点击Edit
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("Edit")').click()
        library = self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/library_grid" )        # 选择第一张照片
        photoes = library.find_elements_by_class_name ( 'android.widget.FrameLayout' )
        photoes[1].click ()  # 选择第一张照片
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/iv_select").click() #打勾
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/menu_sava" ).click ()  # 裁剪，点Next
        filtersView = self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/edit_recyclerView' )
        filters = filtersView.find_elements_by_class_name("android.widget.LinearLayout")
        filters[1].find_element_by_id ( 'com.heavengifts.vaffle:id/filter_image').click() #选择第二个滤镜
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/tv_done" ).click ()  # 点Done
        # self.driver.execute_script ( "mobile: tap", {"touchCount": "1", "x": 536, "y": 390} )        # 选择第一张照片
        # self.driver.execute_script ( "mobile: tap", {"touchCount": "1", "x": 1008, "y": 131} )  #打勾
        # time.sleep(4)
        # self.driver.execute_script ( "mobile: tap", {"touchCount": "1", "x": 1008, "y": 131} )  # 裁剪，点Next
        # time.sleep(4)
        # self.driver.execute_script ( "mobile: tap", {"touchCount": "1", "x": 949, "y": 133} )  # 点Done
        # toast = Findtoast().find_toast(self.driver,"Uploaded profile photo successfully.")
        # if toast=="True":
        #     print("头像修改成功")



    def tearDown(self):
        os.system ( 'start stopAppiumServer.bat' )
        time.sleep(20)
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()