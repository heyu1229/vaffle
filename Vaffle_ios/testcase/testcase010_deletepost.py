import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class IOSTest_deletepost(unittest.TestCase):

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
        # ------------------发布一个post用来删除-------------------------------------------------------
        post_context = ' ios auto test post text for delete'
        post_date = self.public.publish_post(post_context)

        self.driver.find_element_by_ios_predicate("name=='ic more'").click() #点击更多按钮
        self.driver.find_element_by_accessibility_id('Delete').click() #点击删除按钮
        self.driver.save_screenshot('..//testreport/screenshot/test010_deletepost.jpg')
        # self.driver.find_element_by_ios_predicate('Sure').click()
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})
        try:
            self.driver.find_element_by_accessibility_id(post_date+post_context).is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.assertEqual(2, flag, self.write.Write_data(1, 13, 4, '删除失败'))
        self.write.Write_data(1, 13, 4, '删除成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
