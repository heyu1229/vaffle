import os,sys
import unittest,time
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata


class IOSTest_login(unittest.TestCase):

    def setUp(self):
        ios = iostest()
        self.driver=ios.testios()
        # self.public=Publicway(self.driver)
        date = time.strftime('%H%M%S', time.localtime())
        print("当前时间：%s" %date)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))

    def testcase001_login(self):

        # 点菜单进入登录页面
        # self.driver.find_element_by_xpath(
        #     '//XCUIElementTypeOther[@name=" - tab - 5 of 5"]').click()
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        time.sleep(10)
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})
        self.driver.find_element_by_ios_predicate('name=="Settings"').click()
        self.driver.find_element_by_accessibility_id('Log Out').click()
        logout=self.driver.find_elements_by_accessibility_id('Log Out')
        logout[1].click()
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()

        #输入用户名和密码
        # usertext=self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextField'")
        usertext=self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField')
        usertext.clear()
        usertext.send_keys(self.user)
        passtext=self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeSecureTextField'")
        passtext.send_keys(self.password)

        # 点击登陆按钮
        self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Log In\"]").click()

        self.driver.find_element_by_accessibility_id('Hot').click()
        self.driver.save_screenshot('..//testreport/screenshot/test003_login.jpg')
        #添加断言
        try:
            self.driver.find_element_by_accessibility_id('Following').is_displayed()
            flag=1
        except:
            flag=2
        self.assertEqual(1,flag, self.write.Write_data(1, 3, 4, '登录失败'))
        self.write.Write_data(1, 3, 4, '登录成功')
        print("用户" + self.user + "登陆成功")


    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
