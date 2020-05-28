import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait

class IOSTest_deletecomment(unittest.TestCase):

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
        #-------------------------------新发一条纯文本POST------------------------------------------
        post_context=' ios auto test post text for comment delete.'
        self.public.publish_post(post_context)
        # self.driver.find_element_by_accessibility_id('Following').click()
        time.sleep(10)
        #进入第一个POST动态详情页
        self.driver.find_element_by_xpath(
            '(//XCUIElementTypeButton[@name="ic comment"])[1]').click()
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(date+" auto comment.") #输入评论内容
        self.driver.find_element_by_accessibility_id('comment send select').click() #点击评论按钮
        #断言是否评论成功
        time.sleep(3)
        # self.driver.execute_script('mobile:swipe', {'direction': 'up'})
        self.driver.find_element_by_accessibility_id(date+" auto comment.").click()
        # self.driver.save_screenshot('..//testreport/screenshot/test011_deletecomment.jpg')
        self.driver.find_element_by_accessibility_id('Delete').click()
        # self.driver.find_element_by_accessibility_id('Sure').click()
        try:
            self.driver.find_element_by_accessibility_id('1 Comment').is_displayed()  # 点击进入comments列表
            flag=1
        except:
            flag=2
        self.assertEqual(2,flag,self.write.Write_data(1,14,4,'删除评论失败'))
        self.write.Write_data(1, 14, 4, '删除评论成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
