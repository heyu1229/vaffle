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
        self.public=Publicway(self.driver)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))

        # -----------------------录制一段视频---------------------------------------------

    def testcase001_post_takeonevideo(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'
                                                  ).click()
        self.driver.find_element_by_ios_predicate('name=="0"').click()
        # 点击video按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton'
                                          ).click()

        self.driver.find_element_by_ios_predicate('name=="holo start video"').click()  # 点击录像机按钮
        time.sleep(10)
        self.driver.find_element_by_ios_predicate('name=="holo camera going"').click() #录制结束
        self.driver.find_element_by_ios_predicate('name=="holo camera ok"').click()
        time.sleep(6)
        self.driver.find_element_by_ios_predicate('name=="OK(white)"').click() #选择封面
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextView'").send_keys(date)    # 输入文本
        self.driver.find_element_by_ios_predicate('name=="ok(black)"').click()  # 打勾
        # 进入account页面
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        time.sleep(10)
        self.driver.find_element_by_accessibility_id('Account').click()
        time.sleep(3)
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})
        self.driver.save_screenshot('..//testreport/screenshot/test004_publish_takeonevideo.jpg')
        try:
            self.driver.find_element_by_accessibility_id(date).is_displayed()
            flag = 1
        except:
            flag = 2
        self.assertEqual(1, flag,self.write.Write_data(1, 4, 4, '发布录制一段视频失败'))
        self.write.Write_data(1, 4, 4, '发布录制一段视频成功')


    #-----------------------发拍照片的POST---------------------------------------------
    def testcase002_post_takeonephoto(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'
            ).click()
        self.driver.find_element_by_ios_predicate('name=="0"').click()
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton'
            ).click()
        self.driver.find_element_by_ios_predicate('name=="holo camera start"').click()#点击拍照
        self.driver.find_element_by_ios_predicate('name=="holo camera ok"').click() #点击提交照片
        self.driver.find_element_by_ios_predicate('name=="OK(white)"').click()  # 编辑页面点击提交照片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextView'").send_keys(date)  # 输入文本
        self.driver.find_element_by_ios_predicate('name=="ok(black)"').click()  # 打勾
        # 进入account页面
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        time.sleep(10)
        self.driver.find_element_by_accessibility_id('Account').click()
        time.sleep(3)
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})
        self.driver.save_screenshot('..//testreport/screenshot/test004_publish_takeonephoto.jpg')
        try:
            self.driver.find_element_by_accessibility_id(date).is_displayed()
            flag=1
        except:
            flag=2
        self.assertEqual(1, flag,self.write.Write_data(1, 5, 4, '发布拍摄一张图片失败'))
        self.write.Write_data(1, 5, 4, '发布拍摄一张图片成功')

    #-----------------------发布review---------------------------------------------
    def testcase003_post_review(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'
        ).click()
        self.driver.find_element_by_ios_predicate('name=="3"').click()
        # 点击review按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeScrollView/XCUIElementTypeOther[5]'
                                          ).click()
        # self.driver.swipe(60, 545, 60, 545, 500)

        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        text=self.driver.find_elements_by_ios_predicate("type=='XCUIElementTypeTextField'")
        text[0].send_keys(date+'review title') #输入review title
        text[1].send_keys(date+'review name') #输入review name
        text[2].send_keys(date + 'review model') #输入review model
        self.driver.find_element_by_accessibility_id('Write something...').send_keys(date+'review content') #输入review内容

        self.driver.find_element_by_accessibility_id('OK(gray)').click()  # 打勾
        # 进入account页面
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        self.driver.find_element_by_accessibility_id('Account').click()
        time.sleep(3)
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})
        self.driver.execute_script('mobile:swipe', {'direction': 'left'})
        self.driver.execute_script('mobile:swipe', {'direction': 'left'})
        self.driver.save_screenshot('..//testreport/screenshot/test004_publish_review.jpg')
        try:
            self.driver.find_element_by_accessibility_id(date+'review title').is_displayed()
            flag=1
        except:
            flag=2
        self.assertEqual(1, flag,self.write.Write_data(1, 6, 4, '发布review失败'))
        self.write.Write_data(1, 6, 4, '发布review成功')

    #-----------------------发布投票---------------------------------------------
    def testcase004_post_vote(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'
        ).click()
        # 点击投票按钮
        self.driver.find_element_by_ios_predicate('name=="2"').click()

        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        tests=self.driver.find_elements_by_ios_predicate('type=="XCUIElementTypeTextField"')
        tests[1].send_keys(date + 'option2')  # 输入选项2
        self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeTextView'").send_keys(date+'vote')
        tests[0].send_keys(date+'option1') #输入选项1


        self.driver.find_element_by_accessibility_id('ok(black)').click()  # 打勾
        # 进入account页面
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        self.driver.find_element_by_accessibility_id('Account').click()
        time.sleep(3)
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})
        self.driver.save_screenshot('..//testreport/screenshot/test004_publish_vote.jpg')
        try:
            self.driver.find_element_by_accessibility_id(date+'vote').is_displayed()
            flag=1
        except:
            flag=2
        self.assertEqual(1, flag,self.write.Write_data(1, 7, 4, '发布投票失败'))
        self.write.Write_data(1, 7, 4, '发布投票成功')

    def tearDown(self):
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == "__main__":
    unittest.main()