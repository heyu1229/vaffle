import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
import random

class IOSTest_creategroup(unittest.TestCase):

    def setUp(self):

        ios = iostest()
        self.driver=ios.testios()

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)

    # ------------------创建群组-------------------------------------------------------
    def testcase001(self):
        self.driver.find_element_by_ios_predicate("name == 'Hot'").click()
        self.driver.find_element_by_ios_predicate("name=='VGroup'").click()
        self.driver.find_element_by_ios_predicate("name=='discover add'").click()
        # type=self.driver.find_elements_by_ios_predicate("type=='XCUIElementTypeImage'")
        # type[1].click()
        self.driver.find_element_by_ios_predicate("value=='Vape Activity'").click()
        date = time.strftime('%H%M%S', time.localtime())
        t1 = "abcdefghijklnmopqrstuvwxyz"
        t2 = '1234567890'
        r1 = random.choice(t1)
        r2 = random.choice(t2)
        r3 = random.choice(t1)
        r4 = random.choice(t2)
        groupname = r1 + r2 + r3 + r4 + date
        texts=self.driver.find_elements_by_ios_predicate("type=='XCUIElementTypeTextField'")
        texts[0].send_keys(groupname)
        texts[1].click()
        self.driver.find_elements_by_ios_predicate("name=='Sure'")
        # self.driver.swipe(153, 453, 153, 453, 500)
        texts[2].send_keys(groupname + 'brief introduction')
        # self.driver.find_element_by_ios_predicate("value=='Choose a category'").click()
        # self.driver.swipe(153, 453, 153, 453, 500)

        self.driver.find_element_by_ios_predicate("name=='Done'").click()

        try:
            self.driver.find_element_by_accessibility_id('queen').is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.driver.save_screenshot('..//testreport/screenshot/test014_creategroup.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 23, 4, '创建失败'))
        self.write.Write_data(1, 23, 4, '创建成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
