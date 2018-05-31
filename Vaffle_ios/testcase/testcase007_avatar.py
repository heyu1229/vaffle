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
        platformName = 'ios'
        platformVersion = '11.2.1'
        deviceName = 'iPhone'
        udid = 'ce1a52cb2619a04c55ed2d15da938650abbe8c8c'
        app = '..//app/Vape.ipa'
        ios = iostest()
        self.driver = ios.testios(platformName, platformVersion, deviceName, udid, app)
        self.public=Publicway(self.driver)
        self.read = Readdata()
        self.write = Writedata()

        # self.user = self.read.Read_data(0, 2, 0)
        # self.password = int(self.read.Read_data(0, 2, 1))
        # self.public.login_vaffle(self.user, self.password)
    #-----------------------修改头像---------------------------------------------
    def testcase001_update_avatar(self):
        #注册一个新用户
        self.public.sign_up()

        self.driver.find_element_by_accessibility_id('Account').click()  # 点击Account
        table = self.driver.find_element_by_class_name('XCUIElementTypeTable')
        button=table.find_elements_by_class_name('XCUIElementTypeButton')
        button[0].click()
        # self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name=" Edit Profile "]').click()
        self.driver.find_element_by_accessibility_id('Avatar').click()

        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        self.driver.find_element_by_accessibility_id('post photo').click() #点击照相机按钮，进入拍照页面
        # 允许app访问相机/麦克风
        try:
            self.driver.find_element_by_accessibility_id('好').click()
            self.driver.find_element_by_accessibility_id('好').click()
        except:
            print('no notification for camera and microphone')
        self.driver.find_element_by_accessibility_id('camera avatar').click() #点击拍照按钮
        self.driver.find_element_by_accessibility_id('post video ok').click() #点击提交按钮，进入裁剪页面
        self.driver.find_element_by_accessibility_id('Next').click() #点击Next按钮，进入滤镜页面
        filters = self.driver.find_elements_by_class_name("XCUIElementTypeCell")  # 获取所有的滤镜
        filters[1].click()  # 选择第一个滤镜
        self.driver.find_element_by_accessibility_id('done icon').click()  # 点击done提交头像的修改
        time.sleep(30)
        bar=self.driver.find_element_by_class_name('XCUIElementTypeNavigationBar')
        bu=bar.find_elements_by_class_name('XCUIElementTypeButton')
        bu[0].click()
        table = self.driver.find_element_by_class_name('XCUIElementTypeTable')
        button = table.find_elements_by_class_name('XCUIElementTypeButton')
        button[2].click()
        self.driver.find_element_by_accessibility_id('Avatar').click()

        try:
            edit=self.driver.find_element_by_accessibility_id('Edit').text
            self.assertEqual('Edit',edit,self.write.Write_data(1, 19, 4, '修改失败'))
            self.write.Write_data(1, 19, 4, '修改成功')
            print('修改成功')
        except:
            self.write.Write_data(1, 19, 4, '修改失败')
            print('修改失败')

    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat' )
        self.driver.quit()
        # os.system('..//public/stopAppiumServer.bat')


if __name__ == "__main__":
    unittest.main()