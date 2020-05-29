import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
import random

class IOSTest_hot(unittest.TestCase):

    def setUp(self):

        ios = iostest()
        self.driver=ios.testios()

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)

    # ------------------查看首页hot页面-------------------------------------------------------
    def testcase001_hot(self):
    #查看hot页面
        try:
            t=self.driver.find_element_by_ios_predicate('name =="ic more"').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言
        self.driver.save_screenshot('..//testreport/screenshot/test018_hot.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 27, 4, 'hot页面不正常'))
        self.write.Write_data(1, 27, 4, 'hot页面正常')

    #查看following页面
        self.driver.find_element_by_ios_predicate("name == 'Hot'").click()
        self.driver.find_element_by_ios_predicate("name=='Following'").click()
        try:
            t=self.driver.find_element_by_ios_predicate('name =="ic more"').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言
        self.driver.save_screenshot('..//testreport/screenshot/test018_following.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 28, 4, 'following页面不正常'))
        self.write.Write_data(1, 28, 4, 'hot页面正常')

    #查看Vgroup页面
        self.driver.find_element_by_ios_predicate("name == 'Following'").click()
        self.driver.find_element_by_ios_predicate("name=='VGroup'").click()
        try:
            t=self.driver.find_element_by_ios_predicate('name =="ic more"').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言
        self.driver.save_screenshot('..//testreport/screenshot/test018_vgroup.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 29, 4, 'vgroup页面不正常'))
        self.write.Write_data(1, 29, 4, 'vgroup页面正常')

    #查看answer页面
        self.driver.find_element_by_ios_predicate("name == 'VGroup'").click()
        self.driver.find_element_by_ios_predicate("name=='Answer'").click()
        try:
            t=self.driver.find_element_by_ios_predicate('name =="My question"').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言
        self.driver.save_screenshot('..//testreport/screenshot/test018_answer.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 30, 4, 'answer页面不正常'))
        self.write.Write_data(1, 30, 4, 'answer页面正常')

    #查看topic页面
        self.driver.find_element_by_ios_predicate("name == 'Answer'").click()
        self.driver.find_element_by_ios_predicate("name=='Topic'").click()
        try:
            t=self.driver.find_element_by_ios_predicate('name LIKE "* views"').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言
        self.driver.save_screenshot('..//testreport/screenshot/test018_Topic.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 31, 4, 'Topic页面不正常'))
        self.write.Write_data(1, 31, 4, 'Topic页面正常')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
