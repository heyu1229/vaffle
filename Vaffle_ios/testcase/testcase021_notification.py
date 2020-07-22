import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
import random

class IOSTest_notification(unittest.TestCase):

    def setUp(self):

        ios = iostest()
        self.driver=ios.testios()

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)

    # ------------------notification页面-------------------------------------------------------
    def testcase001(self):

        self.driver.find_element_by_ios_predicate("name == ' - tab - 4 of 5'").click()
        self.driver.find_element_by_ios_predicate("name =='Notification'").click()

        try:
            t=self.driver.find_element_by_ios_predicate("name =='discovery more icon'").is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.driver.save_screenshot('..//testreport/screenshot/test018_notification.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 27, 4, '进入通知页面失败'))
        self.write.Write_data(1, 27, 4, '进入通知页面成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
