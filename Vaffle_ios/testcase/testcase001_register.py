import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata


class IOSTest_register(unittest.TestCase):

    def setUp(self):
        platformName1 = 'ios'
        platformVersion1 = '11.2.1'
        deviceName1 = 'iPhone'
        udid1= 'ce1a52cb2619a04c55ed2d15da938650abbe8c8c'
        #iphone6 61bb2263cfd0c8847559aa0da3cb6c7e8366f0ce  se b267314a3c9520839dedbc8bfcdd05d4bdca95ea
        #iphone7 b004f864a71e100079c0f4a347008b147ebe9a39
        app1 = '..//app/Vape.ipa'
        ios = iostest()
        self.driver=ios.testios(platformName1,platformVersion1,deviceName1,udid1,app1)
        self.public=Publicway(self.driver)
        date = time.strftime('%H%M%S', time.localtime())
        print("当前时间：%s" %date)
        self.displayname = "test"+date
        self.email = "test"+date+"@163.com"
        self.password ="111111"
        print("displayname:%s" %self.displayname)
        print("email:%s" %self.email)
        print("password:%s" %self.password)
        self.read = Readdata()
        self.write = Writedata()

    def testcase001_register(self):
        #点菜单进入登录页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()
        #点右上角Sign Up按钮进入注册页面
        self.driver.find_element_by_accessibility_id(" Sign Up").click()
        #输入name/e-mail/password
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[1]').send_keys(self.displayname)
        self.driver.find_element_by_xpath(
           '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[2]').send_keys(self.email)
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField').send_keys(self.password)
        #　收起键盘
        self.driver.find_element_by_accessibility_id(" Sign Up").click()
        self.driver.find_element_by_accessibility_id("Next").click()
        #选择已经18岁
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="agreement"]').click()
        # self.driver.find_element_by_accessibility_id("agreement").click()
        #进入注册2页面点Sign Up按钮  注册成功后进入首页
        self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=' Sign Up']").click()
        #打开me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        texts = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")
        username=texts[0].text
        print(username)
        # assert self.displayname == username
        self.assertEqual(self.displayname,username, self.write.Write_data(1, 1, 4, '注册失败'))
        self.write.Write_data(1, 1, 4, '注册成功')
        print("用户"+self.displayname+"注册成功")

    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat' )
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')
if __name__ == '__main__':
    unittest.main()
