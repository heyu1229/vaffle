import os
import unittest,time
from appium import webdriver
from public.installapp import iostest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

class IOSTest_publish(unittest.TestCase):

    def setUp(self):
        # os.system ( 'start startAppiumServer.bat' )
        time.sleep(10)
        platformName = 'ios'
        platformVersion = '11.2.1'
        deviceName = 'iPhone'
        udid = 'b004f864a71e100079c0f4a347008b147ebe9a39'
        app = '..//app/Vape.ipa'
        ios = iostest()
        self.driver = ios.testios(platformName, platformVersion, deviceName, udid, app)
        self.public=Publicway(self.driver)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 2, 0)
        self.password = int(self.read.Read_data(0, 2, 1))
        self.public.login_vaffle(self.user, self.password)
    #-----------------------发纯文本POST---------------------------------------------
    def testcase001_post_text(self):
        #点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[3]').click()
        #点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        #选择第一张照片后删除,再输入纯文本
        #选择第一张照片
        photos=self.driver.find_elements_by_class_name('XCUIElementTypeCell')
        photos[1].click()
        self.driver.find_element_by_accessibility_id("ok(black)").click() #打勾
        self.driver.find_element_by_accessibility_id("close small picture").click() #删除已选图片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(
            date + ' ios auto test post text') #输入纯文本
        self.driver.find_element_by_accessibility_id("ok(black)").click() #打勾
        try:
            WebDriverWait(self.driver, 120).until_not(
                EC.visibility_of_element_located((By.ID, "Your post is being sent now.")))
        except:
            print('the network error,the post can not publish')
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        self.driver.find_element_by_accessibility_id('Posts').click() #进入POSTS页面
        #由于post页面也动态详情页都得不到文本内容，只能进入转发页面
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"forward\"])[1]").click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：'+texts[1].text)
        self.assertEqual(texts[1].text, date + ' ios auto test post text',self.write.Write_data(1,3,4,'发布失败'))
        self.write.Write_data(1,3,4,'发布成功')

    #-----------------------发拍照片的POST---------------------------------------------
    def testcase002_post_takeonephoto(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[3]').click()
        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        #点击拍照按钮
        self.driver.find_element_by_accessibility_id('post photo').click()
        #允许app访问相机
        try:
            self.driver.find_element_by_accessibility_id('好').click()
        except:
            print('no notification for camera')
        # 允许app访问麦克风
        try:
            self.driver.find_element_by_accessibility_id('好').click()
        except:
            print('no notification for microphone')

        self.driver.find_element_by_accessibility_id('camera avatar').click()#点击拍照
        self.driver.find_element_by_accessibility_id('post video ok').click() #点击提交照片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('UIATextView').send_keys(
            date + ' ios auto test post take one photo')  # 输入文本
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        try:
            WebDriverWait(self.driver, 120).until_not(
                EC.visibility_of_element_located((By.ID, "Your post is being sent now.")))
        except:
            print('the network error,the post can not publish')
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        self.driver.find_element_by_accessibility_id('Posts').click()  # 进入POSTS页面
        # 由于post页面也动态详情页都得不到文本内容，只能进入转发页面
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"forward\"])[1]").click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[1].text)
        self.assertEqual(texts[1].text, date + ' ios auto test post take one photo', self.write.Write_data(1, 4, 4, '发布拍摄一张图片失败'))
        self.write.Write_data(1, 4, 4, '发布成功')

     # -----------------------发送一张选择的图片---------------------------------------------

    def testcase003_post_onephoto(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[3]').click()
        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        # 选择第一张照片后删除,再输入纯文本
        # 选择第一张照片
        photos = self.driver.find_elements_by_class_name('XCUIElementTypeCell')
        photos[1].click()
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(
            date + ' ios auto test post one photo')  # 输入纯文本
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        try:
            WebDriverWait(self.driver, 120).until_not(
                EC.visibility_of_element_located((By.ID, "Your post is being sent now.")))
        except:
            print('the network error,the post can not publish')
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        self.driver.find_element_by_accessibility_id('Posts').click()  # 进入POSTS页面
        # 由于post页面也动态详情页都得不到文本内容，只能进入转发页面
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"forward\"])[1]").click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[1].text)
        self.assertEqual(texts[1].text, date + ' ios auto test post one photo',self.write.Write_data(1, 5, 4, '发布选择一张图片失败'))
        self.write.Write_data(1, 5, 4, '发布成功')

    #-----------------------发布编辑后的图片---------------------------------------------
    def testcase004_post_edit_photo(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[3]').click()
        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        # 选择第一张照片后删除,再输入纯文本
        # 选择第一张照片
        photos = self.driver.find_elements_by_class_name('XCUIElementTypeCell')
        photos[1].click()
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        #编辑图片
        self.driver.find_element_by_accessibility_id("edit small").click()  # 点击编辑按钮
        filters=self.driver.find_elements_by_class_name("XCUIElementTypeCell")  #获取所有的滤镜
        filters[1].click() #选择第一个滤镜
        self.driver.find_element_by_accessibility_id("Tool").click()  # 点击Tool按钮
        self.driver.find_element_by_accessibility_id("rotate").click()  # 旋转90度
        self.driver.find_element_by_accessibility_id("cropped").click()  # 点击裁剪按钮
        self.driver.find_element_by_accessibility_id("OK(white)").click()  # 点击提交按钮
        self.driver.find_element_by_accessibility_id("Done").click()  # 点击Done按钮
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(
            date + ' ios auto test post edit photo')  # 输入纯文本
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        try:
            WebDriverWait(self.driver, 120).until_not(
                EC.visibility_of_element_located((By.ID, "Your post is being sent now.")))
        except:
            print('the network error,the post can not publish')
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        self.driver.find_element_by_accessibility_id('Posts').click()  # 进入POSTS页面
        # 由于post页面也动态详情页都得不到文本内容，只能进入转发页面
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"forward\"])[1]").click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[1].text)
        self.assertEqual(texts[1].text, date + ' ios auto test post edit photo', self.write.Write_data(1, 6, 4, '发布编辑后的图片失败'))
        self.write.Write_data(1, 6, 4, '发布成功')

    def testcase005_post_takeninephotos(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[3]').click()
        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        # 点击拍照按钮
        self.driver.find_element_by_accessibility_id('post photo').click()
        # 允许app访问相机
        try:
            self.driver.find_element_by_accessibility_id('好').click()
        except:
            print('no notification for camera')
        # 允许app访问麦克风
        try:
            self.driver.find_element_by_accessibility_id('好').click()
        except:
            print('no notification for microphone')

        self.driver.find_element_by_accessibility_id('camera avatar').click()  # 点击拍照
        self.driver.find_element_by_accessibility_id('post video ok').click()  # 点击提交照片
        #循环点击8次拍摄照片
        for n in range(1,9):
            self.driver.find_element_by_accessibility_id('tool image').click()  # 点击图片按钮
            self.driver.find_element_by_accessibility_id('post photo').click() # 点击拍照按钮
            self.driver.find_element_by_accessibility_id('camera avatar').click()  # 点击拍照
            self.driver.find_element_by_accessibility_id('post video ok').click()  # 点击提交照片

        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(
            date + ' ios auto test post take nine photos')  # 输入纯文本
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        try:
            WebDriverWait(self.driver, 120).until_not(
                EC.visibility_of_element_located((By.ID, "Your post is being sent now.")))
        except:
            print('the network error,the post can not publish')
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        self.driver.find_element_by_accessibility_id('Posts').click()  # 进入POSTS页面
        # 由于post页面也动态详情页都得不到文本内容，只能进入转发页面
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"forward\"])[1]").click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[1].text)
        self.assertEqual(texts[1].text, date + ' ios auto test post take nine photos', self.write.Write_data(1, 7, 4, '发布拍摄九张图片失败'))
        self.write.Write_data(1, 7, 4, '发布成功')

    def testcase006_post_ninephotoes(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[3]').click()
        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        # 循环选择9张图片
        library_photos=self.driver.find_elements_by_class_name('XCUIElementTypeCell')
        for n in range(1,10):
            library_photos[n].click()
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(
            date + ' ios auto test post nine photos')  # 输入纯文本
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        try:
            WebDriverWait(self.driver, 120).until_not(
                EC.visibility_of_element_located((By.ID, "Your post is being sent now.")))
        except:
            print('the network error,the post can not publish')
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        self.driver.find_element_by_accessibility_id('Posts').click()  # 进入POSTS页面
        # 由于post页面也动态详情页都得不到文本内容，只能进入转发页面
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"forward\"])[1]").click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[1].text)
        self.assertEqual(texts[1].text, date + ' ios auto test post nine photos', self.write.Write_data(1, 8, 4, '发送九张选择的图片失败'))
        self.write.Write_data(1, 8, 4, '发布成功')

        # -----------------------录制一段视频---------------------------------------------

    def testcase007_post_takeonephoto(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[3]').click()
        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")# 点击拍照按钮
        self.driver.find_element_by_accessibility_id('post photo').click()
        # 允许app访问相机
        try:
            self.driver.find_element_by_accessibility_id('好').click()
        except:
            print('no notification for camera')
        # 允许app访问麦克风
        try:
            self.driver.find_element_by_accessibility_id('好').click()
        except:
            print('no notification for microphone')
        self.driver.find_element_by_accessibility_id('post vedio').click()  # 点击录像机按钮
        # 长按录像机按钮
        action = TouchAction(self.driver)
        video_button = self.driver.find_element_by_accessibility_id('post video icon')
        action.long_press(video_button,None,None,16000).perform()
        self.driver.find_element_by_accessibility_id('post video ok').click()
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(
            date + ' ios auto test post take one video')  # 输入纯文本
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        try:
            WebDriverWait(self.driver, 120).until_not(
                EC.visibility_of_element_located((By.ID, "Your post is being sent now.")))
        except:
            print('the network error,the post can not publish')
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        self.driver.find_element_by_accessibility_id('Posts').click()  # 进入POSTS页面
        # 由于post页面也动态详情页都得不到文本内容，只能进入转发页面
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"forward\"])[1]").click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[1].text)
        self.assertEqual(texts[1].text, date + ' ios auto test post take one video',
                         self.write.Write_data(1, 9, 4, '发布录制一段视频失败'))
        self.write.Write_data(1, 9, 4, '发布录制一段视频成功')

    # -----------------------选择一段视频---------------------------------------------
    def testcase008_post_onephoto(self):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[3]').click()
        # 点击允许访问相册
        try:
            self.driver.find_element_by_accessibility_id('好').click()

        except:
            print("no notification")
        # 选择第一张照片后删除,再输入纯文本
        # 选择第一张照片
        photos = self.driver.find_elements_by_class_name('XCUIElementTypeCell')
        photos[1].click()
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(
            date + ' ios auto test post one video')  # 输入纯文本
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        try:
            WebDriverWait(self.driver, 120).until_not(
                EC.visibility_of_element_located((By.ID, "Your post is being sent now.")))
        except:
            print('the network error,the post can not publish')
        # 进入Me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="Vaffle"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

        self.driver.find_element_by_accessibility_id('Posts').click()  # 进入POSTS页面
        # 由于post页面也动态详情页都得不到文本内容，只能进入转发页面
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"forward\"])[1]").click()
        texts = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        print('text：' + texts[1].text)
        self.assertEqual(texts[1].text, date + ' ios auto test post one video',
                         self.write.Write_data(1, 10, 4, '发布录制一段视频失败'))
        self.write.Write_data(1, 10, 4, '发布录制一段视频成功')

    def tearDown(self):
        # os.system ( 'start stopAppiumServer.bat' )
        self.driver.quit()
        os.system('..//public/stopAppiumServer.bat')

if __name__ == "__main__":
    unittest.main()