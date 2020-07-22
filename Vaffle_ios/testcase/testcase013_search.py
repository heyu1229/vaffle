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

        ios = iostest()
        self.driver=ios.testios()

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)
        # self.public.login_vaffle(self.user, self.password)

    # ------------------搜索用户-------------------------------------------------------
    def testcase001_searchpeople(self):
        t = self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button = t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('queen')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        self.driver.find_element_by_accessibility_id('People').click()

        try:
            self.driver.find_element_by_accessibility_id('queen').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.driver.save_screenshot('..//testreport/screenshot/test013_searchpeople.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 16, 4, '搜索失败'))
        self.write.Write_data(1, 16, 4, '搜索成功')

    # ------------------搜索post-------------------------------------------------------
    def testcase002_searchpost(self):
        t=self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button=t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('queen')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮

        try:
            self.driver.find_element_by_ios_predicate("name LIKE '*queen*'").is_displayed()
            flag = 1
        except:
            flag = 2
        self.driver.save_screenshot('..//testreport/screenshot/test013_searchpost.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 17, 4, '搜索失败'))
        self.write.Write_data(1, 17, 4, '搜索成功')

    # ------------------搜索群组-------------------------------------------------------
    def testcase003_searchvgroup(self):
        t=self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button=t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('queen')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        self.driver.find_element_by_accessibility_id('VGroup').click()

        try:
            self.driver.find_element_by_ios_predicate("name LIKE '*queen*'").is_displayed()
            flag = 1
        except:
            flag = 2
        self.driver.save_screenshot('..//testreport/screenshot/test013_searchvgroup.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 18, 4, '搜索失败'))
        self.write.Write_data(1, 18, 4, '搜索成功')

    # ------------------搜索店铺-------------------------------------------------------
    def testcase004_searchstore(self):
        t=self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button=t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('queen')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        self.driver.find_element_by_accessibility_id('VGroup').click()
        self.driver.find_element_by_accessibility_id('Store').click()

        try:
            self.driver.find_element_by_ios_predicate("name LIKE '*queen*'").is_displayed()
            flag = 1
        except:
            flag = 2
        self.driver.save_screenshot('..//testreport/screenshot/test013_searchstore.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 19, 4, '搜索失败'))
        self.write.Write_data(1, 19, 4, '搜索成功')

    # ------------------搜索topic-------------------------------------------------------
    def testcase005_searchtopic(self):
        t=self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button=t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('on')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        self.driver.find_element_by_accessibility_id('VGroup').click()
        self.driver.find_element_by_accessibility_id('Topic').click()

        try:
            self.driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2
        self.driver.save_screenshot('..//testreport/screenshot/test013_searchtopic.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 20, 4, '搜索失败'))
        self.write.Write_data(1, 20, 4, '搜索成功')

    # ------------------搜索qa-------------------------------------------------------
    def testcase006_searchQA(self):
        t=self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button=t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('on')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        self.driver.find_element_by_accessibility_id('VGroup').click()
        self.driver.find_element_by_accessibility_id('Topic').click()
        self.driver.find_element_by_accessibility_id('Q/A').click()

        try:
            self.driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2
        self.driver.save_screenshot('..//testreport/screenshot/test013_searchQA.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 21, 4, '搜索失败'))
        self.write.Write_data(1, 21, 4, '搜索成功')

    # ------------------搜索qa-------------------------------------------------------
    def testcase007_searchAll(self):
        t=self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button=t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('on')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        self.driver.find_element_by_accessibility_id('All').click()

        try:
            self.driver.find_element_by_ios_predicate("name LIKE '*on*'").is_displayed()
            flag = 1
        except:
            flag = 2
        self.driver.save_screenshot('..//testreport/screenshot/test013_searchAll.jpg')
        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 22, 4, '搜索失败'))
        self.write.Write_data(1, 22, 4, '搜索成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
