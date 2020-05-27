import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class IOSTest_editpost(unittest.TestCase):

    def setUp(self):
        # os.system ( 'start startAppiumServer.bat' )
        time.sleep(10)
        platformName = 'ios'
        platformVersion = '11.2.1'
        deviceName = 'iPhone'
        udid = '61bb2263cfd0c8847559aa0da3cb6c7e8366f0ce'
        app = '..//app/Vape.ipa'
        ios = iostest()
        self.driver=ios.testios(platformName,platformVersion,deviceName,udid,app)

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)
        # self.public.login_vaffle(self.user, self.password)

    def testcase001(self):
        # ------------------发布一个post-------------------------------------------------------
        post_context = ' ios auto test post text for edit.'
        post_date = self.public.publish_post(post_context)

        self.driver.find_element_by_ios_predicate("name=='ic more'").click() #点击更多按钮
        self.driver.find_element_by_accessibility_id('Edit').click() #点击删除按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeTextView').clear().send_keys(post_date+' edit post successful.')
        self.driver.find_element_by_accessibility_id('ok(black)').click()
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})
        self.driver.save_screenshot('..//testreport/screenshot/test012_editpost.jpg')
        try:
            self.driver.find_element_by_accessibility_id(post_date+' edit post successful.').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 27, 4, '编辑失败'))
        self.write.Write_data(1, 27, 4, '编辑成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
