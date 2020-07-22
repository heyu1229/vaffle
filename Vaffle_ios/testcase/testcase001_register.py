import os,sys
import unittest,time,random
from appium import webdriver
sys.path.append('..//public')
from installapp import iostest
from publicway import Publicway
from readdata import Readdata
from writedata import Writedata


class IOSTest_register(unittest.TestCase):

    def setUp(self):
        ios = iostest()
        self.driver=ios.testios()
        self.public=Publicway(self.driver)
        date = time.strftime('%H%M%S', time.localtime())
        print("当前时间：%s" %date)
        t1="abcdefghijklnmopqrstuvwxyz"
        t2='1234567890'
        r1=random.choice(t1)
        r2=random.choice(t2)
        r3=random.choice(t1)
        r4=random.choice(t2)
        self.displayname = r1+r2+r3+r4+date
        self.email = self.displayname+"@163.com"
        self.password ="111111"
        print("displayname:%s" %self.displayname)
        print("email:%s" %self.email)
        print("password:%s" %self.password)
        self.read = Readdata()
        self.write = Writedata()

    def testcase001_register(self):

        # # 点击允许推送通知
        # try:
        #     # buttons=driver.find_elements_by_class_name('UIACollectionCell')
        #     # buttons[1].click()
        #     self.driver.find_element_by_accessibility_id('允许').click()
        #
        # except:
        #     print('no notification')
        #
        # # 引导页
        # self.driver.execute_script('mobile:swipe', {'direction': 'left'})
        # self.driver.execute_script('mobile:swipe', {'direction': 'left'})
        # self.driver.execute_script('mobile:swipe', {'direction': 'left'})
        # self.driver.swipe(200, 615, 200, 615, 500)
        #
        # # 取消升级
        # try:
        #     if self.driver.find_element_by_accessibility_id('Confirm').is_displayed():
        #         self.driver.find_element_by_accessibility_id('Cancel').click()
        # except:
        #     print("no update")
        #
        # # 我已18岁
        #     self.driver.swipe(185, 360, 185, 360, 500)

        #点菜单进入登录页面
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        #点右上角Sign Up按钮进入注册页面
        self.driver.find_element_by_ios_predicate("name==' Sign Up'").click()
        #输入name/e-mail/password
        self.driver.find_element_by_ios_predicate("value=='NAME'").send_keys(self.displayname)
        self.driver.find_element_by_ios_predicate("value=='EMAIL'").send_keys(self.email)
        self.driver.find_element_by_ios_predicate("value=='PASSWORD'").send_keys(self.password)
        # self.driver.find_element_by_xpath(
        #     '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[1]').send_keys(self.displayname)
        # self.driver.find_element_by_xpath(
        #    '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[2]').send_keys(self.email)
        # self.driver.find_element_by_xpath(
        #     '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField').send_keys(self.password)
        # #　收起键盘
        self.driver.find_element_by_ios_predicate("name==' Sign Up'").click()
        time.sleep(2)
        self.driver.find_element_by_ios_predicate("name =='Next'").click()
        #选择已经18岁
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="agreement"]').click()

        #进入注册2页面点Sign Up按钮  注册成功后进入首页
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name=" Sign Up"]').click()
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Skip"]').is_displayed()
            flag=1
        except:
            flag=2
        # assert self.displayname == username
        self.assertEqual(1,flag,self.write.Write_data(1, 1, 4, '注册失败'))
        self.write.Write_data(1, 1, 4, '注册成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')
if __name__ == '__main__':
    unittest.main()