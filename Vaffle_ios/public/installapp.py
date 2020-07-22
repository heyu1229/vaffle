#coding=utf-8
import os,subprocess,time,sys
sys.path.append('..//public')
from appium import webdriver

class iostest():

    def testios(self):
        platformName = 'ios'
        platformVersion = '11.2.1'
        deviceName = 'iPhone'
        udid = 'b004f864a71e100079c0f4a347008b147ebe9a39'#'04e0a15aecc6a9aed13733f5ec0e19775d71eb0c'#'61bb2263cfd0c8847559aa0da3cb6c7e8366f0ce'
        app = '..//app/Vape.ipa'
        PATH=lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))
        desired_caps = {}
        # desired_caps['platformName'] =platformName
        # desired_caps['platformVersion'] = platformVersion
        # desired_caps['deviceName'] = deviceName
        # desired_caps['udid'] =udid
        # desired_caps['app'] = PATH(app)#必须先将项目打包ipa，此处传入ipa路径
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        desired_caps['udid'] = udid
        desired_caps['app'] = PATH(app)  # 必须先将项目打包ipa，此处传入ipa路径
        desired_caps['autoAcceptAlerts'] = True#允许app访问手机权限
        desired_caps['noReset']=True
        os.system('..//public/startAppiumServer.bat')
        time.sleep(5)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(20)

        # # 点击允许推送通知
        # try:
        #     # buttons=driver.find_elements_by_class_name('UIACollectionCell')
        #     # buttons[1].click()
        #     driver.find_element_by_accessibility_id('允许').click()
        #
        # except:
        #     print('no notification')
        #
        # # 引导页
        # driver.execute_script('mobile:swipe', {'direction': 'left'})
        # driver.execute_script('mobile:swipe', {'direction': 'left'})
        # driver.execute_script('mobile:swipe', {'direction': 'left'})
        # driver.swipe(200, 615, 200, 615, 500)
        #
        # # 取消升级
        # try:
        #     if driver.find_element_by_accessibility_id('Confirm').is_displayed():
        #         driver.find_element_by_accessibility_id('Cancel').click()
        # except:
        #     print("no update")
        #
        #     # 我已18岁
        #     driver.swipe(185, 360, 185, 360, 500)

        return driver
