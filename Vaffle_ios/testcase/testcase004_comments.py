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
from appium.webdriver.common.touch_action import TouchAction

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
    #-----------------------给POST评论---------------------------------------------
    def testcase001_post_comment(self):
        #-------------------------------新发一条纯文本POST------------------------------------------
        post_context=' ios auto test post text for comment.'
        self.public.publish_post(post_context)

        #进入第一个POST动态详情页
        self.driver.find_element_by_xpath(
            '(//XCUIElementTypeButton[@name="commends"])[1]').click()
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(date+" auto comment.") #输入评论内容
        self.driver.find_element_by_accessibility_id('comment send select').click() #点击评论按钮
        #self.public.swipeUp(10)
        #断言是否评论成功
        time.sleep(3)
        self.driver.find_element_by_accessibility_id('back black').click() #点击返回首页
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="1 Comment"])[1]').click()  # 点击进入comments列表
        comment_context = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        self.assertEqual(comment_context[6].text, date+" auto comment.",self.write.Write_data(1,13,4,'评论失败'))
        self.write.Write_data(1, 13, 4, '评论成功')


    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat')
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')


if __name__ == "__main__":
    unittest.main()