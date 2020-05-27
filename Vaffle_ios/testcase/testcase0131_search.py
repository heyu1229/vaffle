import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class IOSTest_search(unittest.TestCase):

    def setUp(self):
        # os.system ( 'start startAppiumServer.bat' )



        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))

    # ------------------搜索用户-------------------------------------------------------
    def testcase001_searchpeople(self):
        platformName = 'ios'
        platformVersion = '11.2.1'
        deviceName = 'iPhone'
        udid = '61bb2263cfd0c8847559aa0da3cb6c7e8366f0ce'
        app = '..//app/Vape.ipa'
        ios = iostest()
        global driver
        driver = ios.testios(platformName, platformVersion, deviceName, udid, app)

        t = driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button = t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('on')
        driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        driver.find_element_by_accessibility_id('People').click()

        try:
            driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        driver.save_screenshot('..//testreport/screenshot/test013_searchpeople.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 28, 4, '搜索失败'))
        self.write.Write_data(1, 28, 4, '搜索成功')

    # ------------------搜索post-------------------------------------------------------
    def testcase002_searchpost(self):
        driver.find_element_by_accessibility_id('Post').click()
        try:
            driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2
        driver.save_screenshot('..//testreport/screenshot/test013_searchpost.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 29, 4, '搜索失败'))
        self.write.Write_data(1, 29, 4, '搜索成功')

    # ------------------搜索群组-------------------------------------------------------
    def testcase003_searchvgroup(self):

        driver.find_element_by_accessibility_id('VGroup').click()

        try:
            driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2
        driver.save_screenshot('..//testreport/screenshot/test013_searchvgroup.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 30, 4, '搜索失败'))
        self.write.Write_data(1, 30, 4, '搜索成功')

    # ------------------搜索店铺-------------------------------------------------------
    def testcase004_searchstore(self):

        driver.find_element_by_accessibility_id('Store').click()

        try:
            driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2
        driver.save_screenshot('..//testreport/screenshot/test013_searchstore.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 31, 4, '搜索失败'))
        self.write.Write_data(1, 31, 4, '搜索成功')

    # ------------------搜索topic-------------------------------------------------------
    def testcase005_searchtopic(self):

        driver.find_element_by_accessibility_id('Topic').click()

        try:
            driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2
        driver.save_screenshot('..//testreport/screenshot/test013_searchtopic.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 32, 4, '搜索失败'))
        self.write.Write_data(1, 32, 4, '搜索成功')

    # ------------------搜索qa-------------------------------------------------------
    def testcase006_searchQA(self):

        driver.find_element_by_accessibility_id('Q/A').click()

        try:
            driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2
        driver.save_screenshot('..//testreport/screenshot/test013_searchQA.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 33, 4, '搜索失败'))
        self.write.Write_data(1, 33, 4, '搜索成功')
        driver.quit()

    def tearDown(self):
        # driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
