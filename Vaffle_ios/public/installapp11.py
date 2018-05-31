
import unittest,os,subprocess,time
from appium import webdriver

class iostest(unittest.TestCase):
    def testios(self):
        # path=os.getcwd()
        # print(path)
        # os.system (path+'/startAppiumServer.bat')
        os.system('..//public/startAppiumServer.bat')
        time.sleep (10)
        PATH=lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))
        desired_caps = {}
        desired_caps['platformName'] = 'ios'
        desired_caps['platformVersion'] = '11.2.1'
        desired_caps['deviceName'] = 'iPhone'
        # desired_caps['bundleId'] = 'com.heavengifts.vaffle'
        desired_caps['udid'] = '61bb2263cfd0c8847559aa0da3cb6c7e8366f0ce'
        #6p ce1a52cb2619a04c55ed2d15da938650abbe8c8c
        #ios10 61bb2263cfd0c8847559aa0da3cb6c7e8366f0ce
        #'04e0a15aecc6a9aed13733f5ec0e19775d71eb0c'#SE手机   b267314a3c9520839dedbc8bfcdd05d4bdca95ea  iOS11 b004f864a71e100079c0f4a347008b147ebe9a39
        desired_caps['app'] = PATH('..//app/Vape.ipa')#必须先将项目打包ipa，此处传入ipa路径
        desired_caps['autoAcceptAlerts'] = 'true'#允许app访问手机权限
        desired_caps['xcodeOrgId'] = 'DMRRY68BXV'#允许app访问手机权限
        desired_caps['xcodeSigningId'] = 'iPhone Developer'#允许app访问手机权限
        #driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #subprocess.Popen('killall node', shell=True)
        #subprocess.Popen('/Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/build/lib/main.js –address “127.0.0.1” -p “4723” –command-timeout “100”–automation-name “Appium” >/tmp/1.txt', shell = True)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # try:
        #     buttons=driver.find_elements_by_class_name('UIACollectionCell')
        #     buttons[1].click()
        #
        # except:
        #     print('no notification')
    if __name__ == '__main__':
            unittest.main()
