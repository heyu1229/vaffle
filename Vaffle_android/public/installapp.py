import unittest,os
from appium import webdriver


class androidtest(unittest.TestCase):

    def android(self):
        platformName = 'Android'
        platformVersion = '7.0'
        deviceName = '00a82383e298c621'
        app = '..//apps/vaffle-v2.4.3.apk'
        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        desired_caps = {}
        desired_caps['unicodeKeyboard']='true' #安装appium的虚拟键盘
        desired_caps['resetKeyboard']='true'
        desired_caps['platformName'] = platformName  # 设备的系统
        desired_caps['platformVersion'] = platformVersion  # 设备系统的版本号
        desired_caps['deviceName'] = deviceName  # 设备名称Nexus 5X
        desired_caps['app'] = PATH(app)
        # desired_caps['automationName']= 'Uiautomator2'

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        return driver

if __name__ == '__main__':
    unittest.main()
