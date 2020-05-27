import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class IOSTest_collection(unittest.TestCase):

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

    def testcase001_login(self):
        # -------------------------------新发一条纯文本POST------------------------------------------
        post_context = ' ios auto test post text for collection'
        post_date = self.public.publish_post(post_context)

        self.driver.find_element_by_ios_predicate("name=='ic more'").click()
        self.driver.find_element_by_accessibility_id('Collect').click()  # 收藏按钮
        self.driver.find_element_by_accessibility_id('Cancel').click()
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})  # 下拉刷新
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})  # 下拉刷新
        self.driver.find_element_by_ios_predicate("name=='ic more'").click()
        self.driver.save_screenshot('..//testreport/screenshot/test008_collection.jpg')
        try:
            self.driver.find_element_by_accessibility_id('Collected').is_displayed()  # 编辑按钮
            flag=1
        except:
            flag=2

        # 断言是否收藏成功
        self.assertEqual(1,flag, self.write.Write_data(1, 11, 4, '收藏失败'))
        self.write.Write_data(1, 11, 4, '收藏成功')


    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
