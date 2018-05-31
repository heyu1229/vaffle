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
        # os.system ( 'start startAppiumServer.bat' )
        time.sleep(10)
        platformName = 'ios'
        platformVersion = '11.2.2'
        deviceName = 'iPhone'
        udid = 'ce1a52cb2619a04c55ed2d15da938650abbe8c8c'#白色7p'ce1a52cb2619a04c55ed2d15da938650abbe8c8c'#iphone7黑色'b004f864a71e100079c0f4a347008b147ebe9a39'
        app = '..//app/Vape.ipa'
        ios = iostest()
        self.driver=ios.testios(platformName,platformVersion,deviceName,udid,app)
        # self.public=Publicway(self.driver)
        date = time.strftime('%H%M%S', time.localtime())
        print("当前时间：%s" %date)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))

    def testcase001_login(self):
        # 点菜单进入登录页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()
        #输入用户名和密码
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField').send_keys(self.user)
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField').send_keys(self.password)

        # 点击登陆按钮
        self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Log In\"]").click()

        #进入个人中心
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        #添加断言
        text=self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="queen"]')
        username = text.text
        print(username)
        self.assertEqual(self.user,username, self.write.Write_data(1, 2, 4, '登录失败'))
        self.write.Write_data(1, 2, 4, '登录成功')
        print("用户" + self.user + "登陆成功")


    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == '__main__':
    unittest.main()
