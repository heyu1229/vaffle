#coding=utf-8
import os,subprocess,time
from appium import webdriver

class iostest():

    def testios(self,platformName,platformVersion,deviceName,udid,app):
        PATH=lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))
        desired_caps = {}
        desired_caps['platformName'] =platformName
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        #desired_caps['bundleId'] = 'com.heavengifts.vaffle'
        desired_caps['udid'] =udid
        desired_caps['app'] = PATH(app)#必须先将项目打包ipa，此处传入ipa路径
        desired_caps['autoAcceptAlerts'] = 'true'#允许app访问手机权限
        # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # cmdpath = os.getcwd()
        # print(cmdpath+'/startAppiumServer.bat')
        os.system('..//public/startAppiumServer.bat')
        time.sleep (10)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(20)
        # 点击允许推送通知
        try:
            # buttons=driver.find_elements_by_class_name('UIACollectionCell')
            # buttons[1].click()
            driver.find_element_by_accessibility_id('允许').click()

        except:
            print('no notification')
        # 取消升级
        try:
            if driver.find_element_by_accessibility_id('Confirm').is_displayed():
                driver.find_element_by_accessibility_id('Cancel').click()
        except:
            print("no update")
        return driver
