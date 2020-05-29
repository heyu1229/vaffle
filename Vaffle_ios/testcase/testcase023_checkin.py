import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
import random

class IOSTest_checkin(unittest.TestCase):

    def setUp(self):

        ios = iostest()
        self.driver=ios.testios()

        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public = Publicway(self.driver)
        self.driver.implicitly_wait(5)

    # ------------------签到-------------------------------------------------------
    def testcase001(self):
        # s = "select * from vape_members where id='960'"
        # execute_sql = self.public.sql_vaffle(s)
        # print(execute_sql)

        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        self.driver.find_element_by_ios_predicate("name=='Notification'").click()

        try:
            t=self.driver.find_element_by_ios_predicate("name =='discovery more icon'").is_displayed()
            flag = 1
        except:
            flag = 2

        # 断言是否收藏成功
        self.driver.save_screenshot('..//testreport/screenshot/test019_checkin.jpg')
        self.assertEqual(1, flag, self.write.Write_data(1, 38, 4, '进入通知页面失败'))
        self.write.Write_data(1, 38, 4, '进入通知页面成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
