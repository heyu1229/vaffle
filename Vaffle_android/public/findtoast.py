import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class Findtoast(unittest.TestCase):
    # def find_toast(self,driver, text,timeout=30,poll_frequency=0.5):
    #     try:
    #
    #         toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
    #
    #         WebDriverWait ( driver, timeout, poll_frequency ).until ( EC.presence_of_element_located ( toast_loc ) )
    #         return True
    #
    #     except:
    #         return False

    def find_toast(self,driver, message,timeout, poll_frequency):

        try:
            # element = WebDriverWait ( driver,timeout,poll_frequency).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))

            message = '//*[@text=\'{}\']'.format ( message)
            element = WebDriverWait ( driver, timeout, poll_frequency ).until (
                expected_conditions.presence_of_element_located ( (By.XPATH, message) ) )
            print(element.text)
            return True

        except:

            return False
if __name__ == '__main__':
    unittest.main()

'''
    def find_toast(self,driver, text,timeout=30,poll_frequency=0.05):
        is toast exist, return True or False

           :Agrs:

            - driver - 传driver

            - text   - 页面上看到的文本内容

            - timeout - 最大超时时间，默认30s

            - poll_frequency  - 间隔查询时间，默认0.5s查询一次

           :Usage:

            is_toast_exist(driver, "看到的内容")

   

        try:
            print("aaaaaaa")

            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)

            WebDriverWait ( driver, timeout, poll_frequency ).until ( EC.presence_of_element_located ( toast_loc ) )

            print("ccccc")

            return True

        except:

            print("dddddd")

            return False
       
'''
