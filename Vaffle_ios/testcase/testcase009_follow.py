import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class IOSTest_follow(unittest.TestCase):

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

    def testcase001(self):
        # ------------------搜索一个用户然后进行关注-------------------------------------------------------
        t = self.driver.find_element_by_ios_predicate("name=='Soul.WOLHomeView'")
        button = t.find_elements_by_ios_predicate("type=='XCUIElementTypeButton'")
        button[1].click()
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'").send_keys('queen001')
        self.driver.swipe(330, 640, 330, 640, 500)  # 搜索按钮
        self.driver.find_element_by_accessibility_id('People').click()
        self.driver.find_element_by_accessibility_id('ic post follow').click() #点击关注按钮
        # self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeImage'
        #                                   ).click()
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})
        try:
            self.driver.find_element_by_accessibility_id('eachother').click()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.assertEqual(1, flag, self.write.Write_data(1, 12, 4, '关注失败'))
        self.write.Write_data(1, 12, 4, '关注成功')
        self.driver.save_screenshot('..//testreport/screenshot/test009_follow.jpg')
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Unfollow "]').click() #取消关注
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
