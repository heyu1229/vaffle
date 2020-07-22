import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

class IOSTest_avatar(unittest.TestCase):

    def setUp(self):
        # platformName = 'ios'
        # platformVersion = '11.2.1'
        # deviceName = 'iPhone'
        # udid = 'b004f864a71e100079c0f4a347008b147ebe9a39'#'61bb2263cfd0c8847559aa0da3cb6c7e8366f0ce'
        # app = '..//app/Vape.ipa'
        ios = iostest()
        self.driver = ios.testios()
        self.public=Publicway(self.driver)
        self.read = Readdata()
        self.write = Writedata()

        # self.user = self.read.Read_data(0, 2, 0)
        # self.password = int(self.read.Read_data(0, 2, 1))
        # self.public.login_vaffle(self.user, self.password)
    #-----------------------修改头像---------------------------------------------
    def testcase001_update_avatar(self):
        #注册一个新用户
        # self.public.sign_up()
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        self.driver.find_element_by_accessibility_id('Account').click()  # 点击Account
        # self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Add"])[1]').click()

        adds=self.driver.find_elements_by_ios_predicate("name=='Add'")
        adds[0].click()
        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        self.driver.find_element_by_ios_predicate("name=='holo photo select'").click() #点击照相机按钮，进入拍照页面
        # 允许app访问相机/麦克风
        try:
            self.driver.find_element_by_accessibility_id('好').click()
            self.driver.find_element_by_accessibility_id('好').click()
        except:
            print('no notification for camera and microphone')
        self.driver.find_element_by_ios_predicate("name=='holo camera start'").click() #点击拍照按钮
        self.driver.find_element_by_ios_predicate("name=='holo camera ok'").click() #点击提交按钮，进入裁剪页面

        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Done"]').click()  # 点击done提交头像的修改
        time.sleep(30)
        self.driver.save_screenshot('..//testreport/screenshot/test002_avatar.jpg')

        try:
            self.driver.find_element_by_ios_predicate("name=='Done'").is_displayed() #点击进入like页面
            flag=1
        except:
            flag=2

        self.assertEqual(1, flag,self.write.Write_data(1, 2, 4, '修改失败'))
        self.write.Write_data(1, 2, 4, '修改成功')
        print('修改成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == "__main__":
    unittest.main()