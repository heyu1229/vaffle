import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
import random

class IOSTest_grouppost(unittest.TestCase):

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
        self.driver.implicitly_wait(5)

    # ------------------发布群组post-------------------------------------------------------
    def testcase001(self):
        #搜索一个群组
        t = self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button = t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('uuu')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        self.driver.find_element_by_accessibility_id('VGroup').click()
        #进入群聊
        self.driver.find_element_by_ios_predicate("name LIKE 'uuu'").click()
        self.driver.find_element_by_ios_predicate("name=='cameracolor'").click()
        date = time.strftime('%H%M%S', time.localtime())

        # 选择第一张照片
        self.driver.find_element_by_ios_predicate("name=='next white'").click()
        self.driver.find_element_by_ios_predicate("name=='OK(white)'").click()  # 编辑页面点击提交照片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextView'").send_keys(date+'group')  # 输入文本
        self.driver.find_element_by_ios_predicate("name=='ok(black)'").click()  # 打勾
        self.driver.find_element_by_ios_predicate("name=='back1'").click() #返回
        self.driver.find_element_by_ios_predicate("name=='back black'").click()
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        self.driver.find_element_by_accessibility_id("Account").click()
        time.sleep(2)
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})

        try:
            self.driver.find_element_by_accessibility_id(date+'group').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.driver.save_screenshot('..//testreport/screenshot/test015_grouppost.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 35, 4, '发布失败'))
        self.write.Write_data(1, 35, 4, '发布成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
