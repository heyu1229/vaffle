import os
import unittest,time
from appium import webdriver
from public.installapp import androidtest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class AndroidTest_register(unittest.TestCase):

    def setUp(self):
        os.system ( 'start startAppiumServer.bat' )
        time.sleep ( 10 )
        Android = androidtest()
        self.driver=Android.android()
        self.public=Publicway(self.driver)
        date = time.strftime('%H%M%S', time.localtime())
        print("当前时间：%s" %date)
        self.displayname = "lisa"+date
        self.email = "lisa"+date+"@163.com"
        self.password ="111111"
        print("displayname:%s" %self.displayname)
        print("email:%s" %self.email)
        print("password:%s" %self.password)

    def testcase001_register(self):
        self.driver.implicitly_wait(10)
        try:
            if self.driver.find_element_by_xpath("//*[@text='Updates']").is_displayed():
                self.driver.find_element_by_xpath("//*[@text='Cancel']").click()
        except:
            print("no update")
        # self.driver.find_element_by_id("com.heavengifts.vaffle:id/update_cancel").click()

        #点菜单进入登录页面
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/bottom_menu_me").click()
        #点右上角Sign Up按钮进入注册页面
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/menu_right").click()
        #输入name/e-mail/password

        names = self.driver.find_element_by_id("com.heavengifts.vaffle:id/l_param1")
        names.find_element_by_id("com.heavengifts.vaffle:id/ed_content").send_keys(self.displayname)

        emails = self.driver.find_element_by_id("com.heavengifts.vaffle:id/l_param2")
        emails.find_element_by_id("com.heavengifts.vaffle:id/ed_content").send_keys(self.email)

        passwords = self.driver.find_element_by_id("com.heavengifts.vaffle:id/l_param3")
        passwords.find_element_by_id("com.heavengifts.vaffle:id/ed_content").send_keys(self.password)

        self.driver.find_element_by_id("com.heavengifts.vaffle:id/btn_sign_before").click()

        #进入注册2页面点Sign Up按钮  注册成功后进入首页
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/ct_certification").click()         #勾选我已满18周岁
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/btn_register").click()
        #断言进入Me页面
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/bottom_menu_me").click()

        #标题显示用户nickanme
        # titles = self.driver.find_element_by_id("com.heavengifts.vaffle:id/toolbar")
        # title = titles.find_element_by_class_name("android.widget.TextView").text
        # assert "Me"==title
        #头像旁边显示的是displayname
        assert self.displayname == self.driver.find_element_by_id("com.heavengifts.vaffle:id/nickname").text
        print("用户注册成功")
    def tearDown(self):
        os.system ( 'start stopAppiumServer.bat' )
        time.sleep(20)
        # self.driver.quit()
