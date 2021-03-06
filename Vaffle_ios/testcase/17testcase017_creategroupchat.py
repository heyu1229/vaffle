import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
import random

class IOSTest_creategroupchat(unittest.TestCase):

    def setUp(self):

        ios = iostest()
        self.driver=ios.testios()

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)

    # ------------------创建群聊-------------------------------------------------------
    def testcase001(self):

        self.driver.find_element_by_ios_predicate("name == ' - tab - 4 of 5'").click()
        self.driver.find_element_by_ios_predicate("name =='Start a chat'").click()
        time.sleep(5)
        self.driver.find_element_by_ios_predicate("name =='Create a group chat'").click()#点击创建群聊按钮
        time.sleep(5)
        buttons=self.driver.find_elements_by_ios_predicate("name =='status no selected'")
        buttons[0].click()
        time.sleep(2)
        el=self.driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="Create a group chat"]')
        bs=el.find_elements_by_ios_predicate("type =='XCUIElementTypeButton'")
        bs[1].click()
        date = time.strftime('%H%M%S', time.localtime())
        self.driver.find_element_by_ios_predicate("value=='Group chat name, 1-50 characters (required)'").send_keys(date+'groupchat')
        self.driver.swipe(335, 44, 335, 44, 500)

        try:
            self.driver.find_element_by_ios_predicate("name LIKE '*groupchat(2)'").is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.driver.save_screenshot('..//testreport/screenshot/test017_creategroupchat.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 26, 4, '创建群聊失败'))
        self.write.Write_data(1, 26, 4, '创建群聊成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
