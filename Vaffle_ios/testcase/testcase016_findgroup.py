import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
import random

class IOSTest_findgroup(unittest.TestCase):

    def setUp(self):

        ios = iostest()
        self.driver=ios.testios()

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)

    # ------------------发现群组-------------------------------------------------------
    def testcase001(self):

        self.driver.find_element_by_ios_predicate("name == 'Hot'").click()
        self.driver.find_element_by_ios_predicate("name =='VGroup'").click()
        self.driver.find_element_by_ios_predicate("name =='ic discover small group'").click()#点击发现群组按钮

        try:
            self.driver.find_element_by_accessibility_id('Group category').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.driver.save_screenshot('..//testreport/screenshot/test016_findgroup.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 25, 4, '进入发现页面失败'))
        self.write.Write_data(1, 25, 4, '进入发现页面成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
