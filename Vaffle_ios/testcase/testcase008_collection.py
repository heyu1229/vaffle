import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class IOSTest_collection(unittest.TestCase):

    def setUp(self):
        # os.system ( 'start startAppiumServer.bat' )
        time.sleep(10)
        platformName = 'ios'
        platformVersion = '11.2.1'
        deviceName = 'iPhone'
        udid = 'ce1a52cb2619a04c55ed2d15da938650abbe8c8c'
        app = '..//app/Vape.ipa'
        ios = iostest()
        self.driver=ios.testios(platformName,platformVersion,deviceName,udid,app)

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)
        self.public.login_vaffle(self.user, self.password)

    def testcase001_login(self):
        # -------------------------------新发一条纯文本POST------------------------------------------
        post_context = ' ios auto test post text for collection'
        post_date = self.public.publish_post(post_context)

        #点击收藏
        self.driver.find_element_by_xpath(
            '(//XCUIElementTypeButton[@name="notToCollect"])[1]').click()
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()
        self.driver.find_element_by_accessibility_id('Collection').click()
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="forward"])[1]').click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[1].text)
        # 断言是否收藏成功
        self.assertEqual(texts[1].text, post_date + " ios auto test post text for collection", self.write.Write_data(1, 13, 4, '收藏失败'))
        self.write.Write_data(1, 13, 4, '收藏成功')


    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
