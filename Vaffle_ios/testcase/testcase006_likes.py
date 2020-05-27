import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

class IOSTest_publish(unittest.TestCase):

    def setUp(self):
        ios = iostest()
        self.driver = ios.testios()
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)
        # self.public.login_vaffle(self.user, self.password)
    #-----------------------给POST点赞---------------------------------------------
    def testcase001_post_likes(self):
        # -------------------------------新发一条纯文本POST------------------------------------------
        post_context = ' ios auto test post text for like.'
        self.public.publish_post(post_context)
        # self.driver.find_element_by_accessibility_id('Following').click()
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="ic like"])[1]').click() #点击like按钮
        time.sleep(3)
        self.driver.save_screenshot('..//testreport/screenshot/test006_likes.jpg')
        try:
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="1"]').is_displayed() #点击进入like页面
            flag=1
        except:
            flag=2
        self.assertEqual (1, flag,self.write.Write_data(1,9,4,'点赞失败'))
        self.write.Write_data(1, 9, 4, '点赞成功')


    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat' )
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')


if __name__ == "__main__":
    unittest.main()