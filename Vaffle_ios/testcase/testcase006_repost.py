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

class IOSTest_publish(unittest.TestCase):

    def setUp(self):
        platformName = 'ios'
        platformVersion = '11.2.1'
        deviceName = 'iPhone'
        udid = 'ce1a52cb2619a04c55ed2d15da938650abbe8c8c'
        app = '..//app/Vape.ipa'
        ios = iostest()
        self.driver = ios.testios(platformName, platformVersion, deviceName, udid, app)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)
        self.public.login_vaffle(self.user, self.password)
    #-----------------------转发post---------------------------------------------
    def testcase001_post_repost(self):
        # -------------------------------新发一条纯文本POST------------------------------------------
        post_context = ' ios auto test post text for repost.'
        post_date=self.public.publish_post(post_context)

        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="forward"])[1]').click()#点击转发按钮
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(date+' auto repost.') #输入转发的文本
        self.driver.find_element_by_accessibility_id('ok(black)').click()#点击发送按钮
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[1]').click()
        # self.driver.find_element_by_accessibility_id('Posts').click()  # 进入POSTS页面

        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="forward"])[1]').click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[2].text)
        #断言是否转发成功
        self.assertEqual (texts[2].text, post_date + ' ios auto test post text for repost.',self.write.Write_data(1,17,4,'转发失败'))
        self.write.Write_data(1, 17, 4, '转发成功')


    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat' )
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')


if __name__ == "__main__":
    unittest.main()