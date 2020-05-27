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
    #-----------------------转发post---------------------------------------------
    def testcase001_post_repost(self):
        # -------------------------------新发一条纯文本POST------------------------------------------
        post_context = ' ios auto test post text for repost.'
        post_date=self.public.publish_post(post_context)

        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="ic forward"])[1]').click()#点击转发按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="Repost"]').click()#转发repost
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(date+' auto repost.') #输入转发的文本
        self.driver.find_element_by_accessibility_id('ok(black)').click()#点击发送按钮
        time.sleep(3)
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})  # 下拉刷新
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})  # 下拉刷新
        # self.driver.find_element_by_accessibility_id("Combined Shape Copy").click()
        # self.driver.find_element_by_accessibility_id("Account").click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="Selected - - tab - 1 of 5"]').click()

        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="ic more"]').click()
        self.driver.find_element_by_accessibility_id('Edit').click() #编辑按钮
        text=self.driver.find_element_by_class_name('XCUIElementTypeTextView').text
        print('转发的文案：',text)
        self.driver.save_screenshot('..//testreport/screenshot/test007_repost.jpg')
        #断言是否转发成功
        self.assertEqual (text, date + ' auto repost.',self.write.Write_data(1,10,4,'转发失败'))
        self.write.Write_data(1, 10, 4, '转发成功')


    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat' )
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')


if __name__ == "__main__":
    unittest.main()