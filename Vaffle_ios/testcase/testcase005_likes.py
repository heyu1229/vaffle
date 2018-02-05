import os
import unittest,time
from appium import webdriver
from public.installapp import iostest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

class IOSTest_publish(unittest.TestCase):

    def setUp(self):
        platformName = 'ios'
        platformVersion = '11.2.1'
        deviceName = 'iPhone'
        udid = 'b004f864a71e100079c0f4a347008b147ebe9a39'
        app = '..//app/Vape.ipa'
        ios = iostest()
        self.driver = ios.testios(platformName, platformVersion, deviceName, udid, app)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)
        self.public.login_vaffle(self.user, self.password)
    #-----------------------给POST点赞---------------------------------------------
    def testcase001_post_likes(self):
        # -------------------------------新发一条纯文本POST------------------------------------------
        post_context = ' ios auto test post text for like.'
        self.public.publish_post(post_context)

        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="love"])[1]').click() #点击like按钮
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="1 Like"])[1]').click() #点击进入like页面
        #得到displayname
        displayname = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")
        #断言是否点赞成功
        print(displayname[6].text)
        self.assertEqual (displayname[6].text, '@'+self.user,self.write.Write_data(1,15,4,'点赞失败'))
        self.write.Write_data(1, 15, 4, '点赞成功')


    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat' )
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')


if __name__ == "__main__":
    unittest.main()