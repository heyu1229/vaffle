import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
import random

class IOSTest_discover(unittest.TestCase):

    def setUp(self):

        ios = iostest()
        self.driver=ios.testios()

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)

    # ------------------查看首页发现页面-------------------------------------------------------
    def testcase001_discover(self):

        self.driver.find_element_by_ios_predicate("name == ' - tab - 3 of 5'").click()
        try:
            t=self.driver.find_element_by_ios_predicate('name =="ic_video"').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言
        self.driver.save_screenshot('..//testreport/screenshot/test020_discover.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 33, 4, 'discover页面不正常'))
        self.write.Write_data(1, 33, 4, 'discover页面正常')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
